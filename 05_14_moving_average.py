import pybithumb

# get ohlcv는 웹스크래핑을 통해 오래된 거래 데이터를 가져온다.
# Open, High, Low, Close, Volume

btc = pybithumb.get_ohlcv("BTC")
print(btc)

close = btc['close']
print(close)

