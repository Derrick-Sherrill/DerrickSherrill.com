import yfinance as yf
import pandas as pd

df = pd.read_csv('companylist.csv')

print(df['Symbol'])
increased_volume = []

for stock in df['Symbol']:
    stock = stock.upper()
    if '^' in stock:
        pass
    else:
        try:
            stock_info = yf.Ticker(stock)
            hist = stock_info.history(period="5d")
            previous_averaged_volume = hist['Volume'].iloc[1:4:1].mean()
            todays_volume = hist['Volume'][-1]
            previous_close = hist['Close'][-2]
            current_close = hist['Close'][-1]
            if todays_volume > previous_averaged_volume * 4 and previous_close < current_close and todays_volume > 100000:
                print(stock)
                print(previous_averaged_volume)
                print(todays_volume)
                increased_volume.append(stock)
        except:
            pass

print(increased_volume)
