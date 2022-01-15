import requests
import datetime

r = requests.get("https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw")
bitcoin = r.json()
print(type(bitcoin))
print(bitcoin)
print("비트코인 거래량 \n")
timestamp = bitcoin['timestamp']
date = datetime.datetime.fromtimestamp(timestamp/1000)
print("최종체결시간: ", date)

print("최종체결가: ", bitcoin['last'])
print("매수호가: ", bitcoin['bid'])
print("매도호가: ", bitcoin['ask'])
print("거래량: ", bitcoin['volume'])