import time
import pybithumb

# API Key 값
con_key = "dcf8aaf072f8b00c7b34f1b6d21e19f1"
sec_key = "d124474264f75e438b4fcea43aeeaa46"

Bithumb = pybithumb.Bithumb(con_key, sec_key)

# 나의 특정 ticker의 자산, 거래중인수량, 보유중인총원화, 주문에사용된총원화)
balance = Bithumb.get_balance("ADA")
print("나의 ADA 현황: ", balance)

# for ticker in pybithumb.get_tickers():
#     balance2 = bithumb.get_balance(ticker)
#     print(ticker, ":", balance2)
#     time.sleep(0.1)

# 주문을 해보자
# order = bithumb.buy_limit_order("KLAY", 1671, 1)
# " bid, klay, 주문번호 - 주문조회/취소/정정에 사용됨, KRW 원화"
# ('bid', 'KLAY', 'C0538000000030396139', 'KRW')
# print(order)

# {'status': '5600', 'message': '최소 주문금액은 500 KRW 입니다.'}
order = Bithumb.buy_limit_order("ADA", 1210, 3)
# order = Bithumb.sell_limit_order("KLAY",1730, 2, "KRW")
print(order)

# get order book