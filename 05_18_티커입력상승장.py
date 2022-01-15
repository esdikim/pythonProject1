import pybithumb

def bull_market(ticker):
    # 5일 이동편균값을 계산한다 ma5
    # 전일 이동 평균값을 구한다 last_ma5

    df = pybithumb.get_ohlcv(ticker)
    ma5 = df['close'].rolling(window=5).mean()

    # ticker 현재가를 가져온다
    price = pybithumb.get_current_price(ticker)

    last_ma5 = ma5[-2]  # 전일의 이동 평균값은 ma5 끝에서 두번째

    if price > last_ma5:
        return True
    else:
        return False

is_bull = bull_market("BTC")
if is_bull:
    print("상승장")
else:
    print("하락장")

# 티커를 가져와서 상승장인지 하락장인지 판단해 본다
tickers = pybithumb.get_tickers()

ii = 0
jj = 0
for ticker in tickers:
    is_bull = bull_market(ticker)
    if is_bull:
        print(ticker, "상승장")
        ii = ii +1
    else:
        print(ticker, "하락장")
        jj = jj+1

print("상승종목: ", ii)
print("하락종목: ", jj)