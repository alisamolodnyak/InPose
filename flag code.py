import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5 import uic

class Flag(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('flag.ui', self)
        self.setFixedSize(900, 900)
        self.pushButton.clicked.connect(self.get_flag)
        self.buttonGroup_2.buttonClicked.connect(self.set_color)
        self.buttonGroup_3.buttonClicked.connect(self.set_color)
        self.buttonGroup.buttonClicked.connect(self.set_color)
        self.data = {self.buttonGroup: 'Синий', self.buttonGroup_3: 'Синий', self.buttonGroup_2: 'Синий'}
    def set_color(self, button):
        self.data[self.sender()]=button.text()
    def get_flag(self):
        self.answer.setText(" ".join(self.data.values()))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Flag()
    ex.show()
    sys.exit(app.exec_())