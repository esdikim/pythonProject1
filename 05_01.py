# pybithumb
# 05_01
# python으로 빗썸의 정보를 가져온다

import pybithumb
import time

tickers = pybithumb.get_tickers()
print(tickers)
print("전체 ticker의 갯수는 len(tickers) : ", len(tickers))
tickers2 = pybithumb.get_tickers('KRW')
print(tickers2)
print("전체 ticker의 갯수는 : ", len(tickers2))

price = pybithumb.get_current_price("BTC")
print("\n 비트코인의 현재가를 가져온다.")
print(price)

i = 0
# while i < 10:
#     price = pybithumb.get_current_price("BTC")
#     print("BTC ", i, price)
#     time.sleep(1)
#     i=i+1

for ticker in tickers:
    price = pybithumb.get_current_price(ticker)
    print(ticker, price)
    time.sleep(0.1)

