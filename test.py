import yfinance as yf
#from pandas_datareader import data as pdr
f = open("stocks.txt", "r")
stocks = f.read()
stocks = stocks.split("\n")
for stock in stocks:
    stock = stock + ".OL"
    print(stock)
    try:
      msft = yf.Ticker(stock)
      print(msft.info['forwardPE'])
    except:
      print("Error")