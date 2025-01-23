import pandas as pd

class Tickers:
    def __init__(self):
        self.SP_OneHundred = pd.read_html('https://en.wikipedia.org/wiki/S%26P_100')[2]['Symbol']
        self.SP_FiveHundred = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]['Symbol']
        self.SP_SixHundred = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_600_companies')[0]['Symbol']
        self.NAS_OneHundred = pd.read_html('https://en.wikipedia.org/wiki/Nasdaq-100')[4]['Ticker']
        self.Rus_OneThousand = pd.read_html('https://en.wikipedia.org/wiki/Russell_1000_Index')[2]['Ticker']
        self.Dow = pd.read_html('https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average')[1]['Symbol']
 