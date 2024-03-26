import sys
from gallery import Gallery
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import os
import sys
import time
from comparing import compare_image_with_others

class MyCamera(QCamera):
    def paintEvent(self, QPaintEvent):
        painter = QtGui.QPainter(self)
        pen = QtGui.QPen()
    #    pen.setColor(QtGui.Qt.green)
        painter.setPen(pen)
        painter.drawLine(100, 100, 300, 100)



class Example(QMainWindow):
    takePhoto: QPushButton
    cameraLayout: QVBoxLayout
    def __init__(self):
        super().__init__()
        uic.loadUi('camera_int.ui', self)
        self.contour_name = None
        self.available_cameras = QCameraInfo.availableCameras()
        # if no camera found
        if not self.available_cameras:
            # exit the code
            sys.exit()
        # creating a status bar
        # self.status = QStatusBar()
        # setting style sheet to the status bar
        # self.status.setStyleSheet("background : white;")

        # adding status bar to the main window
        # self.setStatusBar(self.status)

        # path to save
        self.save_path = os.path.abspath("")
        print(self.save_path)

        # creating a QCameraViewfinder object
        self.viewfinder = QCameraViewfinder()
        #self.Camera.show()
        # showing this viewfinder
        self.viewfinder.show()

        # making it central widget of main window
        """ЭТО САМОЕ ГЛАВНОЕ"""
        self.cameraLayout.addWidget(self.viewfinder)

        # Set the default camera.
        self.select_camera(0)
        # self.draw_something()
        # setting window title
        self.setWindowTitle("PyQt5 Cam")

        self.takePhoto.clicked.connect(self.click_photo)

        # showing the main window
        self.show()

        pixmap = QtGui.QPixmap(1, 1)
        self.marker_label = QLabel(self)
        painter = QtGui.QPainter(pixmap)
        # painter.setPen(QtGui.QPen(Qt.green, 4, Qt.SolidLine))
        painter.drawEllipse(pixmap.rect().adjusted(4, 4, -4, -4))
        painter.end()
        self.marker_label.setPixmap(pixmap)

    def mousePressEvent(self, event):
        self.marker_label.move(event.pos() - self.marker_label.rect().center())
        self.marker_label.show()
        super().mousePressEvent(event)

    # def draw_something(self):
    #     painter = QtGui.QPainter(self.cameraLayout.pixmap())
    #     painter.drawLine(10, 10, 300, 200)
    #     painter.end()


        # method to select camera
    def set_contour(self, image_name):
        x = image_name.find(".")
        self.contour_name = image_name[:x] + "_contour.png"
        print(self.contour_name)

        pixmap = QtGui.QPixmap(os.path.join("contours_all", self.contour_name))
        #pixmap = QtGui.QPixmap(300, 300)
        print(pixmap)
        self.marker_label = QLabel(self)
        self.marker_label.resize(pixmap.width(), pixmap.height())
        self.marker_label.setPixmap(pixmap)
        self.marker_label.move(0, 300)
        self.marker_label.show()
    def select_camera(self, i):

        # getting the selected camera
        self.camera = MyCamera(self.available_cameras[i])

        # setting view finder to the camera
        self.camera.setViewfinder(self.viewfinder)

        # setting capture mode to the camera
        self.camera.setCaptureMode(MyCamera.CaptureStillImage)

        # if any error occur show the alert
        self.camera.error.connect(lambda: self.alert(self.camera.errorString()))

        # start the camera
        self.camera.start()


        # creating a QCameraImageCapture object
        self.capture = QCameraImageCapture(self.camera)

        # showing alert if error occur
        self.capture.error.connect(lambda error_msg, error,
                                          msg: self.alert(msg))

        # when image captured showing message
        self.capture.imageCaptured.connect(lambda d,
                                                  i: print("Image captured : " + str(self.save_seq)))

        # getting current camera name
        self.current_camera_name = self.available_cameras[i].description()

        # initial save sequence
        self.save_seq = 0

        # method to take photo

    def click_photo(self):


        # capture the image and save it on the save path
        self.capture.capture(os.path.join(self.save_path,
                                          "photo.jpg"))

        # increment the sequence
        self.save_seq += 1
        x = compare_image_with_others("photo.jpg", number_of_offered=20)
        self.gallery = Gallery(x, parent=self)
        self.gallery.show()
        self.marker_label.move(300, 300)
        self.marker_label.show()
        # change folder method

    def change_folder(self):

        # open the dialog to select path
        path = QFileDialog.getExistingDirectory(self,
                                                "Picture Location", "")

        # if path is selected
        if path:
            # update the path
            self.save_path = path

            # update the sequence
            self.save_seq = 0

        # method for alerts

    def alert(self, msg):

        # error message
        error = QErrorMessage(self)

        # setting text to the error message
        error.showMessage(msg)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())