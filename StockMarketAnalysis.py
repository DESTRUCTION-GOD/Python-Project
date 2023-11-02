import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def analyze_stock():
    stock_symbol = input("Enter the stock symbol (e.g., AAPL for Apple Inc.): ")

    start_date = "2020-01-01"
    end_date = "2021-12-31"

    data = yf.download(stock_symbol, start=start_date, end=end_date)

    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    data['SMA_200'] = data['Close'].rolling(window=200).mean()

    data['Daily_Return'] = data['Close'].pct_change()

    data['Cumulative_Return'] = (1 + data['Daily_Return']).cumprod() - 1

    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'], label='Stock Price', color='blue')
    plt.plot(data.index, data['SMA_50'], label='50-Day SMA', color='orange')
    plt.plot(data.index, data['SMA_200'], label='200-Day SMA', color='red')
    plt.title(f'{stock_symbol} Stock Price and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

    plt.figure(figsize=(12, 4))
    plt.plot(data.index, data['Daily_Return'], label='Daily Returns', color='green')
    plt.title(f'{stock_symbol} Daily Returns')
    plt.xlabel('Date')
    plt.ylabel('Returns')
    plt.legend()
    plt.show()

    plt.figure(figsize=(12, 4))
    plt.plot(data.index, data['Cumulative_Return'], label='Cumulative Returns', color='purple')
    plt.title(f'{stock_symbol} Cumulative Returns')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Returns')
    plt.legend()
    plt.show()

analyze_stock()