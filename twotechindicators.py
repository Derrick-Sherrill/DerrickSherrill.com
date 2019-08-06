import pandas as pd
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt

api_key = 'RNZPXZ6Q9FEFMEHM'

period = 60

ti = TechIndicators(key=api_key, output_format='pandas')

data_ti, meta_data_ti = ti.get_rsi(symbol='MSFT', interval='1min',
                                    time_period=period, series_type='close')

data_sma, meta_data_sma = ti.get_sma(symbol='MSFT', interval='1min',
                                    time_period=period, series_type='close')

df1 = data_sma.iloc[1::]
df2 = data_ti
df1.index = df2.index

fig, ax1 = plt.subplots()
ax1.plot(df1, 'b-')
ax2 = ax1.twinx()
ax2.plot(df2, 'r.')
plt.title("SMA & RSI graph")
plt.show()
