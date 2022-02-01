# 백트래킹 준비
# 1
# 2

import pybithumb
import datetime


df = pybithumb.get_ohlcv("KLAY")
print(df.tail(5))
# print(df.tail())
df['range'] = (df['high']-df['low'])*0.5
df['range_shift'] = df['range'].shift(1)
df['target'] = df['open'] + df['range_shift']

df.to_excel("klay1.xlsx")