import datetime

import pybithumb


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
