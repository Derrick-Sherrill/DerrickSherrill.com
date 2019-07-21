import plotly
import plotly.graph_objects as go
import pandas as pd

excel_file = 'ProductSales.xlsx'
df = pd.read_excel(excel_file)
print(df)

data = [go.Scatter( x=df['Date'], y=df['Profit'])]

fig = go.Figure(data)
#fig.show()

plotly.offline.plot(fig, filename="Salesreport.html")
