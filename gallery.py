import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from resize import resize_image
from PyQt5.QtGui import QPalette, QColor

class Color(QtWidgets.QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)
class Gallery(QtWidgets.QMainWindow):
    def __init__(self, chosen_images, parent=None):
        self.parent = parent
        self.number_of_images = 0
        self.chosen_image = None
        super(Gallery, self).__init__(parent)
        highlight_dir = os.path.join("all")
        uic.loadUi('gallery.ui', self)
        columns_layout = QtWidgets.QHBoxLayout()
        self.gallery_column_layouts = [QtWidgets.QVBoxLayout(), QtWidgets.QVBoxLayout()]

        for i in self.gallery_column_layouts:
            i.setContentsMargins(0, 0, 0, 0)

        for i in self.gallery_column_layouts:
            columns_layout.addLayout(i)


        #self.scrollArea = QtWidgets.QScrollArea(widgetResizable=True)
        content_widget = QtWidgets.QWidget()
        content_widget.setLayout(columns_layout)
        self.scrollArea.setWidget(content_widget)
        self._lay = QtWidgets.QVBoxLayout(content_widget)

        self.files_it = iter([os.path.join(highlight_dir, file)
                              for file in filter(lambda x: x in chosen_images, os.listdir(highlight_dir))])

        self._timer = QtCore.QTimer(self, interval=1)
        self._timer.timeout.connect(self.on_timeout)
        self._timer.start()

    def on_timeout(self):
        try:
            file = next(self.files_it)
            pixmap = QtGui.QPixmap(file)
            pixmap = pixmap.scaledToWidth(200)
            label = QtWidgets.QLabel()
            label.mousePressEvent = self.get_clicked_function(file.split("\\")[-1])
            label.setPixmap(pixmap)
            self.gallery_column_layouts[self.number_of_images % len(self.gallery_column_layouts)].addWidget(label)
            self.number_of_images += 1
        except StopIteration:
            self._timer.stop()

    def get_clicked_function(self, filename):
        def foo(*args):
            print(filename)
            self.chosen_image = filename
            if self.parent:
                print(self.parent)
                self.parent.set_contour(self.chosen_image)
            self.hide()
        return foo

    def add_pixmap(self, pixmap):
        if not pixmap.isNull():
            label = QtWidgets.QLabel(pixmap=pixmap)
            self._lay.addWidget(label)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)



if __name__ == '__main__':
    import sys
    sys.excepthook = except_hook
    app = QtWidgets.QApplication(sys.argv)
    w = Gallery(['00036.jpg', '00094.jpg', '00099.jpg', '00126.jpg', '00031.jpg', '00068.jpg'])
    w.show()
    sys.exit(app.exec_())


