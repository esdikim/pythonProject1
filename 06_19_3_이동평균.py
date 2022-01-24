# 5일 평균선을 구한다.

import pybithumb

df = pybithumb.get_ohlcv("KLAY")
print(df)
close = df['close']
ma5 = close.rolling(5).mean()
print(ma5)