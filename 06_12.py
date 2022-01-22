import pybithumb
import time

ii = 0
while ii < 10:
    price = pybithumb.get_current_price("KLAY")
    print(price)
    time.sleep(0.2)
    ii += 1

df = pybithumb.get_ohlcv("KLAY")
print(df.tail())
