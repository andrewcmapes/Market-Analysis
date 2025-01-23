import pandas as pd
import numpy as np
import yfinance as yf

def Market_50():
    tickers = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]['Symbol'].replace(['BRK.B', 'BF.B'], ['BRK-B', 'BF-B'])
    random_values = np.random.choice(range(0, 502), 50, replace=False)
    stock_picks = tickers[random_values].tolist()
    
    data = yf.download(stock_picks, period='5y', interval='1mo', progress=False)['Adj Close'][::12].dropna(axis=1)
    portfolio_return = 1
    for i in range(0, 4):
        individual_returns = (data.iloc[i+1,:]-data.iloc[i,:])/data.iloc[i,:]
        portfolio_return = sum((1/len(data.iloc[0,:]))*(individual_returns + 1))*portfolio_return
    portfolio_return = portfolio_return-1
    market = yf.download('SPY', period='5y', interval='1mo', progress=False)['Adj Close'][::12]
    market_return = (market.iloc[-1]-market.iloc[0])/market.iloc[0]
    # print(f'Portfolio return is {np.round(portfolio_return*100,2)}%')
    # print(f'Market return is {np.round(market_return*100,2)}%')
    return portfolio_return, market_return

gain = 0
loss = 0
for i in range(100):
    x,y = Market_50()
    if x > y:
        gain += 1
    else:
        loss += 1
    print(gain/(gain+loss))