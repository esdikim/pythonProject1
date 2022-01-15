import requests
from bs4 import BeautifulSoup


url = "https://finance.naver.com/item/main.nhn?code=000660"
html = requests.get(url).text

soup = BeautifulSoup(html, "html5lib")
tags = soup.select("#tab_con1 > div:nth-child(3) > table > tbody > tr.strong > td > em")  #태그를 찾음. 유일한 class가 있으니 .class를 이용한다.

# 루프를 돌면서 tags를 tag에 넣고, test를 찍어준다. 많이 나온다.
for tag in tags:
    print(tag)
    print(tag.text)

#tab_con1 > div:nth-child(3) > table > tbody > tr.strong > td > em
# https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw

