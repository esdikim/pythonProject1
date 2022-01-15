import pybithumb

# get ohlcv는 웹스크래핑을 통해 오래된 거래 데이터를 가져온다.
# Open, High, Low, Close, Volume

btc = pybithumb.get_ohlcv("BTC")

close = btc['close']

# 5일씩 묶는 윈도우를 설정합니다.

print("# 5일씩 묶는 윈도우를 설정합니다.")
window = close.rolling(5)
print(window)

ma5 = window.mean()
print("평균값", ma5)

ma6 = close.rolling(5).mean()
print(ma6)

