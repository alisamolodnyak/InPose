import sys
from camera_class import Camera
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5 import uic
import os
print(os.listdir())
print(os.path.abspath("date.py"))

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('camera_old.ui', self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())


