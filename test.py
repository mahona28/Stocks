import yfinance as yf
#from pandas_datareader import data as pdr

msft = yf.Ticker("2020.OL")
print(msft.info)