'''
Tutorial Video for this script:
https://youtu.be/3eV3_yfGM4s

Description:
Useful for multivariate data, this script creates an andrew's curve from an excel
spreadsheet using the pandas plotting methods.
'''

import pandas as pd # Import pandas
from pandas.plotting import andrews_curves # Importing Plotting method
import matplotlib.pyplot as plt # Required for pandas.plotting

excel_file = 'CableLog.xlsx' # Denote Exel file
# If not in same directory:
# excel_file = 'excel_file_path/excel_file.xlsx'

df = pd.read_excel(excel_file) # Creates Dataframe
print(df) # Verify that excel file has been read in

plt.figure() # Creates a figure
andrews_curves(df, 'Quality Test') # Adds an Andrew's curve to the figure

plt.show() # Shows the figure
