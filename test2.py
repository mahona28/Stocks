import yfinance as yf
stock = yf.Ticker("YAR.OL")
print(stock.info['quickRatio'])