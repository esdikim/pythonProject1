# ch03/03_23.py
# 비트코인의 실시간 시세를 조회해 온다.

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pykorbit

form_class = uic.loadUiType("mywindow.ui")[0]

class MyWindow(QMainWindow, form_class):
     def __init__(self):
         super().__init__()
         self.setupUi(self)

         self.timer = QTimer(self)
         self.timer.start(1000)
         self.timer.timeout.connect(self.inquery)

     def inquery(self):
         cur_time = QTime.currentTime()
         str_time = cur_time.toString("hh:mm:ss")
         self.statusBar().showMessage(str_time)

         price = pykorbit.get_current_price("BTC")
         self.lineEdit.setText(str(price))

         price2 = pykorbit.get_current_price("ETH")
         self.lineEdit_2.setText(str(price2))

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()