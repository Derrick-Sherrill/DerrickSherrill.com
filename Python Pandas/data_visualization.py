import pandas as pd
import matplotlib.pyplot as plt

excel_file_path = "Financial Sample.xlsx"
df = pd.read_excel(excel_file_path)
#print(df)

# Time series
df_vtt_canada = df.loc[(df['Country'] == 'Canada') & (df['Product'] == 'VTT') & (df['Segment'] == 'Government')]
df_vtt_canada = df_vtt_canada.sort_values(by=['Date'])
#df_vtt_canada.plot(x='Date', y='Profit')
#plt.show()

df_products = df.groupby(['Product']).sum()
df_products['Units Sold'].plot.pie()
plt.show()
