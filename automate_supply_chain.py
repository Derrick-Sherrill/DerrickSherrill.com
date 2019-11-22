'''
Partial talk through of how I used this script found in this video:
https://youtu.be/x01N1kIQhUs

Description:
AWS SageMaker script I used in automating a supply chain at my previous employer
'''

%matplotlib inline

import sys
from urllib.request import urlretrieve
import zipfile
from dateutil.parser import parse
import json
from random import shuffle
import random
import datetime
import os



import boto3
import s3fs
import sagemaker
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from ipywidgets import IntSlider, FloatSlider, Checkbox

np.random.seed(1)

!conda install -y s3fs

import boto3
import s3fs
import sagemaker
from sagemaker import get_execution_role

"""Input your own file path
in the below lines

bucket='{{{bucket_name}}}7'
prefix = 'prysmian-forecasting' #Used for denoting storage location

sagemaker_session = sagemaker.Session()
role = get_execution_role()

folder1='sagemaker' #First Directory within Bucket
folder2='data' # Second Directory within bucket
folder3='train' # Third Directory within Bucket
data_key = 'RawMaterialItems.xlsx' #File name


s3_data_path = 's3://{}/{}/{}/{}/{}'.format(bucket, folder1, folder2, folder3, data_key)
s3_output_path = "{}/{}/output".format(bucket, prefix)
"""

from sagemaker.amazon.amazon_estimator import get_image_uri
image_name = get_image_uri(boto3.Session().region_name, 'forecasting-deepar')

freq = 'M'  #Our spreadsheet uses raw month in YY-MMM format. Cannot process this with pandas so I changed it to month end
prediction_length = 5 #How many months into the future we want to predict into the future
context_length = 12 #How much context we want to supply to the algorithm - Year is more than enough

data = pd.read_excel(s3_data_path, parse_dates=True, index_col=0) #Sets index column as the first column in spreadsheet (The Dates)
num_timeseries = data.shape[1] #Looks at the shape of the first column of data to determine the number of time series
data_length=data.index.size #Determines the dynamic length of data in each time series (changes and gets smarter month to month)
print("This is the number of time series you're running through the algorithm (This many materials):")
print(num_timeseries)
print("This is the # of months of data that your spreadsheet has:")
print(data_length)
t0 = data.index[0]
print("This is the beginning date:")
print(t0)
time_series=[] #Defines the structure of the time series data

for i in range(num_timeseries):
    index = pd.DatetimeIndex(start=t0, freq=freq, periods=data_length)
    time_series.append(pd.Series(data=data.iloc[:,i], index=index)) #Must treat this dynamically, so for loop (Length changes monthly)

print(time_series[2]) #Visual to make sure data is loaded correctly. No Graph = no bueno amigo
time_series[2].plot()
plt.show()

time_series_training = [] #Creates structure of our training data
for ts in time_series:
    time_series_training.append(ts[:-prediction_length]) #appends everything except the prediction length, default of five months because that's what we're predicting

time_series[2].plot(label='test')
time_series_training[2].plot(label='train', ls=':') #Fancy way of determining what we want the model to predict later
plt.legend()
plt.show()

def series_to_obj(ts, cat=None):
    obj = {"start": str(ts.index[0]), "target": list(ts)}
    if cat is not None:
        obj["cat"] = cat
    return obj

def series_to_jsonline(ts, cat=None):
    return json.dumps(series_to_obj(ts, cat)) #Most annoying process is conversion to JSON data type - makes it easier to dump excel data

encoding = "utf-8"  #Takes JSON to unicode b/c have to encode data for s3 writing
s3filesystem = s3fs.S3FileSystem()  # Data: Excel -> Dataframe -> series appended -> JSON -> UTF-8 byte type -> S3 Bucket JSON. Brutal Dude

with s3filesystem.open(s3_data_path + "/train/train.json", 'wb') as fp:
    for ts in time_series_training:
        fp.write(series_to_jsonline(ts).encode(encoding))
        fp.write('\n'.encode(encoding))

with s3filesystem.open(s3_data_path + "/test/test.json", 'wb') as fp:
    for ts in time_series:
        fp.write(series_to_jsonline(ts).encode(encoding))
        fp.write('\n'.encode(encoding))

estimator = sagemaker.estimator.Estimator(
    sagemaker_session=sagemaker_session,
    image_name=image_name,
    role=role,
    train_instance_count=1,
    train_instance_type='ml.c4.xlarge',
    base_job_name='DEMO-deepar',
    output_path="s3://" + s3_output_path
)

hyperparameters = {
    "time_freq": freq,
    "context_length": str(context_length),
    "prediction_length": str(prediction_length),
    "num_cells": "40",
    "num_layers": "3",
    "likelihood": "gaussian",
    "epochs": "80",
    "mini_batch_size": "32",
    "learning_rate": "0.001",
    "dropout_rate": "0.05",
    "early_stopping_patience": "10"
}

estimator.set_hyperparameters(**hyperparameters)

%%time
data_channels = {

    "train": "{}/train/".format(s3_data_path),
    "test": "{}/test/".format(s3_data_path)
}

estimator.fit(inputs=data_channels, wait=True)

job_name = estimator.latest_training_job.name

endpoint_name = sagemaker_session.endpoint_from_job(
    job_name=job_name,
    initial_instance_count=1,
    instance_type='ml.m4.xlarge',
    deployment_image=image_name,
    role=role
)

class DeepARPredictor(sagemaker.predictor.RealTimePredictor):

    def set_prediction_parameters(self, freq, prediction_length):
        """Set the time frequency and prediction length parameters. This method **must** be called
        before being able to use `predict`.

        Parameters:
        freq -- string indicating the time frequency
        prediction_length -- integer, number of predicted time points

        Return value: none.
        """
        self.freq = freq
        self.prediction_length = prediction_length

    def predict(self, ts, cat=None, encoding="utf-8", num_samples=100, quantiles=["0.1", "0.75", "0.9"]):
        """Requests the prediction of for the time series listed in `ts`, each with the (optional)
        corresponding category listed in `cat`.

        Parameters:
        ts -- list of `pandas.Series` objects, the time series to predict
        cat -- list of integers (default: None)
        encoding -- string, encoding to use for the request (default: "utf-8")
        num_samples -- integer, number of samples to compute at prediction time (default: 100)
        quantiles -- list of strings specifying the quantiles to compute (default: ["0.1", "0.5", "0.9"])

        Return value: list of `pandas.DataFrame` objects, each containing the predictions
        """
        prediction_times = [x.index[-1]+1 for x in ts]
        req = self.__encode_request(ts, cat, encoding, num_samples, quantiles)
        res = super(DeepARPredictor, self).predict(req)
        return self.__decode_response(res, prediction_times, encoding)

    def __encode_request(self, ts, cat, encoding, num_samples, quantiles):
        instances = [series_to_obj(ts[k], cat[k] if cat else None) for k in range(len(ts))]
        configuration = {"num_samples": num_samples, "output_types": ["quantiles"], "quantiles": quantiles}
        http_request_data = {"instances": instances, "configuration": configuration}
        return json.dumps(http_request_data).encode(encoding)

    def __decode_response(self, response, prediction_times, encoding):
        response_data = json.loads(response.decode(encoding))
        list_of_df = []
        for k in range(len(prediction_times)):
            prediction_index = pd.DatetimeIndex(start=prediction_times[k], freq=self.freq, periods=self.prediction_length)
            list_of_df.append(pd.DataFrame(data=response_data['predictions'][k]['quantiles'], index=prediction_index))
        return list_of_df


 predictor = DeepARPredictor(
    endpoint=endpoint_name,
    sagemaker_session=sagemaker_session,
    content_type="application/json"
)
predictor.set_prediction_parameters(freq, prediction_length)

list_of_df = predictor.predict(time_series_training[:60])
actual_data = time_series[:5]

for k in range(len(list_of_df)):
    plt.figure(figsize=(12,6))
    actual_data[k][-prediction_length-context_length:].plot(label='target')
    p10 = list_of_df[k]['0.1']
    p90 = list_of_df[k]['0.9']
    plt.fill_between(p10.index, p10, p90, color='y', alpha=0.5, label='80% confidence interval')
    list_of_df[k]['0.75'].plot(label='prediction median')
    plt.legend()
    plt.show()


print(predictor.predict(time_series[:4
                                   ]))

sagemaker_session.delete_endpoint(endpoint_name)  #Save my bank account and run this command whenever you're done
