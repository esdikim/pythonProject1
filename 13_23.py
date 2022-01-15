# ch03/03_23.py
# 비트코인의 실시간 시세를 조회해 온다.

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pykorbit

form_class = uic.loadUiType("mywindow.ui")[0]

class MyWindow(QMainWindow, form_class):
     def __init__(self):
         super().__init__()
         self.setupUi(self)
         self.pushButton.clicked.connect(self.inquiry)

     def inquiry(self):
         price = pykorbit.get_current_price("BTC")
         self.lineEdit.setText(str(price))
         print(price)

         price2 = pykorbit.get_current_price("ETH")
         self.lineEdit_2.setText(str(price2))
         print(price2)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()