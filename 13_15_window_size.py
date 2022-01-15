import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *   # ICON File import

# QMainWindow를 상속받아서 MyWindow를 구성한다.
# super() 부모 클래스의 init 메소드를 사용하게다.
# 생성자가 이미 부모클래스에서 있으니, 그걸 사용하겠다는것임. (?)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,200,400,400)
        self.setWindowTitle("Stock Auto Trading System")
        self.setWindowIcon(QIcon("Stock_Title_Icon.png"))

        btn = QPushButton("버튼1", self)
        btn.move(50,100)

        btn = QPushButton("버튼2", self)
        btn.move(50,150)

app = QApplication(sys.argv)

window = MyWindow()
window.show()

app.exec_()


