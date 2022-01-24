# 2022.1.22 변동값 계산, 래리윌리엄스의 변동성 돌파 전략
# 주석은 CTRL + /
"""
주석으로 사용한다
"""

import datetime
import time
import pybithumb

# 타켓 가격을 함수로 만들어서 사용한다.
def get_tartet_price(ticker):
    df = pybithumb.get_ohlcv(ticker)
    yesterday = df.iloc[-2]  # 전일값
    print(yesterday)

    today_open = yesterday['close']  # 어제의 종가가 오늘이 시가가 된다. 어제의 종가와ㅏ 오늘의 시가는 같다.
    yesterday_high = yesterday['high']  # 어제의 고가
    yesterday_low = yesterday['low']  # 어제의 저가

    target = today_open + (yesterday_high - yesterday_low) * 0.5  # 변동값 * 0.5 => 목표가격,
    print("today: ", today_open)
    # print(target)
    return target


target_price = get_tartet_price("KLAY")
print("target: ", target_price)

dt = datetime.datetime(2022, 1, 21)
print(dt)

print(dt.year, dt.month, dt.day, dt.time())

now = datetime.datetime.now()
print(now)

print(now == dt)
print(now > dt)

mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
print(mid)

ii = 0
while True:
    now = datetime.datetime.now()
    if mid < now < mid + datetime.datetime.delta(second=10):
        print("정각입니다.")
        now = datetime.datetime.now()
        mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)

    print("ii = :", ii, now, "vs", mid)
    time.sleep(1)

    if ii > 20:
        break

    ii += 1

print("종료합니다.", ii)


