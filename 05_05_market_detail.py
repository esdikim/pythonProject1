# pybithumb
# 05_05
# python으로 빗썸의 정보를 가져온다
# 빗섬으로부터 티커의 시가, 고가, 저가, 종가, 거래양을 가져올 수 있다.
import datetime

import pybithumb
import time

tickers = pybithumb.get_tickers()
print(tickers)
print("전체 ticker의 갯수는 len(tickers) : ", len(tickers))
tickers2 = pybithumb.get_tickers('KRW')
print(tickers2)
print("전체 ticker의 갯수는 : ", len(tickers2))

price = pybithumb.get_market_detail("BTC")
print("\n 비트코인의 시가, 고가, 저가, 종가, 거래량을 가져온다.")
print(price)

orderbook = pybithumb.get_orderbook("BTC")
print(orderbook)

print(" orderbook을 순서대로 찍어준다")
for k in orderbook:
    print(k)

times = int(orderbook['timestamp'])
print(times)
times2 = times/1000/86000/365
print("1970년 1월 1일 이후 몇일이 지났는지 계산, 밀리세컨이니 .. 1000으로 나누고,,, 86000초, 365일을 나누면 됨")
print(times2)

dt = datetime.datetime.fromtimestamp(times/1000)
print(dt)

bids = orderbook['bids']
asks = orderbook['asks']

print(bids)
print(asks)

for bid in bids:
    price = bid['price']
    quant = bid['quantity']
    print("매수호가: ", price, "매수잔량 ", quant)

for ask in asks:
    price = ask['price']
    quant = ask['quantity']
    print("*매도호가: ", price, "매도잔량 ", quant)

i = 57414000.0*0.3974
print(i)

j = 57349000.0*0.0066
print(j)