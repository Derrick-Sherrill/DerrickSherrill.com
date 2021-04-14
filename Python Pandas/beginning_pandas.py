import pandas as pd
import plotly.express as px

df_gold_prices = pd.read_csv('monthly_gold_prices.csv')

# Viewing data
print(df_gold_prices.tail(20))

dates = df_gold_prices['Date']
prices = df_gold_prices['Price']

# simple operations
df_gold_prices['buy_price'] = prices * .9
print(df_gold_prices['Price'].max())
df_gold_prices['Date'] = df_gold_prices['Date'].str.replace('-', '')

print(df_gold_prices)

fig = px.line(df_gold_prices, x = dates, y = prices, title = 'Gold Prices over Time')
fig.show()
