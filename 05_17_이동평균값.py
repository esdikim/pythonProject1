import pybithumb

# 5일 이동편균값을 계산한다 ma5
# 전일 이동 평균값을 구한다 last_ma5
df = pybithumb.get_ohlcv("BTC")
ma5 = df['close'].rolling(5).mean()
last_ma5 = ma5[-2]  # 전일의 이동 평균값은 ma5 끝에서 두번째

# 비트코인의 현재가를 가져온다
price = pybithumb.get_current_price("BTC")
print("이전 5일 평균값 : ", last_ma5)
print("비트코인 현재가 : ", price)
# 5일 이동평균값을 보고 현재가와 비교하여 상승장인지 하락장인지를 구한다
if price > last_ma5:
    print("상승장")
else:
    print("하락장")

diff = price - last_ma5
print("차이 : ", diff)
