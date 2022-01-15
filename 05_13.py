import pybithumb
import time

ii = 0
while True:
    price = pybithumb.get_current_price("BTC")
    try:
        print(price/10)
    except:
        print("에러발생", price)
    time.sleep(0.2)

    ii = ii+1
    if ii == 10:
        break

print("program 정상종료")