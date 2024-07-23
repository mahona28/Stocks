import yfinance as yf
#get the stocks from stocks.txt
f = open("stocks.txt", "r")
stocks = f.read()
stocks = stocks.split("\n")
quickratio = [[],[]]
currentRatio = [[],[]]
debtToEquity = [[],[]]
operatingProfitMargins = [[],[]]
for stock in stocks:
    stock = stock + ".OL"
    #print(stock)
    try:
      msft = yf.Ticker(stock)
      print(msft.info['quickRatio'])
      quickratio += [[stock][msft.info['quickRatio']]]
      # print(msft.info['currentRatio'])
      # currentRatio += [[stock],[msft.info['currentRatio']]]
      # print(msft.info['debtToEquity'])
      # debtToEquity += [[stock],[msft.info['debtToEquity']]]
      # print(msft.info['operatingProfitMargins'])
      # operatingProfitMargins += [[stock],[msft.info['operatingProfitMargins']]] 

    except:
      print("Error")
print(quickratio)
f.close()