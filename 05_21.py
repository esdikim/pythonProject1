import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pybithumb

tickers = ["BTC", "ETH", "BCH", "ADA", "KLAY"]
form_class = uic.loadUiType("bull.ui")[0]

class MyWindow(QMainWindow, form_class):
     def __init__(self):
         super().__init__()
         self.setupUi(self)

         timer = QTimer(self)
         timer.start(5000)
         timer.timeout.connect(self.timeout)

     def get_market_infos(self, ticker):
         df = pybithumb.get_ohlcv(ticker)
         ma5 = df['close'].rolling(window=5).mean()  #5일 이동평균선을 구한다.
         last_ma5 = ma5[-2] #전날의 이동평균
         price = pybithumb.get_current_price(ticker) #현재의 가격을 가져온다

         state = None # 초기값

         if price > last_ma5:
             state = "상승장"
         else:
             state = "하락장"

         return price, last_ma5, state

     def timeout(self):
         for i, ticker in enumerate(tickers):
             print(i, ticker)
             ticker_item = QTableWidgetItem(ticker)
             # print(ticker_item)
             self.tableWidget.setItem(i, 0, ticker_item)  # 0은 0행 0열, 1행 1열 (0,0)(0,1)(1,0)(1,1)

             price, last_ma5, state = self.get_market_infos(ticker)
             self.tableWidget.setItem(i, 1, QTableWidgetItem(str(price)))
             self.tableWidget.setItem(i, 2, QTableWidgetItem(str(last_ma5)))
             self.tableWidget.setItem(i, 3, QTableWidgetItem(state))

app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()