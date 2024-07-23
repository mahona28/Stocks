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
      print(msft.info['quickRatio'])
      print(msft.info['currentRatio'])
      print(msft.info['debtToEquity'])
      print(msft.info['operatingProfitMargins'])

    except:
      print("Error")
f.close()