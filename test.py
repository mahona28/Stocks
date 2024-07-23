import yfinance as yf
#get the stocks from stocks.txt
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
f.close()