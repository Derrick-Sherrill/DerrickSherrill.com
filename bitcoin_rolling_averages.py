import pandas as pd

excel_file = 'BTC_USD_2013-10-01_2019-07-23-CoinDesk.csv'

df = pd.read_csv(excel_file)
print(df.columns)
print(df.head(5))

new_df = df.loc[:, "Date":"Closing Price (USD)"]
print(new_df)

simple_moving_average = new_df.rolling(window=7, on='Date').mean()
print(simple_moving_average)
