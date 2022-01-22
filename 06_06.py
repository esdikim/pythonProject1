import time
import pybithumb

# API Key 값
con_key = "dcf8aaf072f8b00c7b34f1b6d21e19f1"
sec_key = "d124474264f75e438b4fcea43aeeaa46"

bithumb = pybithumb.Bithumb(con_key, sec_key)

mymoney = bithumb.get_balance("KLAY")[2]
print("0 주문가능잔고: ", mymoney)
orderbook = pybithumb.get_orderbook("KLAY")
print("1 매수호가내역: ", orderbook)
asks = orderbook['asks']
print("2 : ", asks)
sell_price = asks[0]['price']
print("3: ", sell_price)
unit = mymoney/sell_price
print(unit)

# 결과값
# {'timestamp': '1642245060253',
#  'payment_currency': 'KRW',
#  'order_currency': 'KLAY',
#
#  'bids':   # 매수요청
#      [{'price': 1687.0, 'quantity': 6302.4366},
#       {'price': 1686.0, 'quantity': 5891.9619},
#       {'price': 1685.0, 'quantity': 7881.5518},
#       {'price': 1684.0, 'quantity': 3021.2837},
#       {'price': 1683.0, 'quantity': 3562.5149}],
#
#  'asks':    # 매도요청
#      [{'price': 1688.0, 'quantity': 1036.3403},
#       {'price': 1689.0, 'quantity': 4450.064498815867},
#       {'price': 1690.0, 'quantity': 4284.51},
#       {'price': 1691.0, 'quantity': 1149.9094},
#       # {'price': 1692.0, 'quantity': 2322.2038}]}