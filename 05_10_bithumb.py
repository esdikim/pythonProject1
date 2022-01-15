import pybithumb

all = pybithumb.get_current_price("ALL")

print("bithumb의 모든 코인의 가격을 가져온다.")
ii = 0
for ticker, data in all.items():
    print(ticker,data['closing_price'])
    ii = ii+1

print("전체코인은: " , ii, '개')