import sys
from PyQt5 import QtCore, QtGui, QtMultimedia, QtMultimediaWidgets, QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget
from PyQt5.QtMultimedia import QCamera, QCameraInfo, QMediaObject, QCameraViewfinderSettings, QCameraImageCapture
from PyQt5.QtMultimediaWidgets import QCameraViewfinder


class Camera(QObject):
    def __init__(self, parent = QObject()):
        super(Camera, self).__init__(parent)
        self.cam = QCamera(QCameraInfo.defaultCamera())
        self.caminfo = QCameraInfo(self.cam)
        self.camvfind = QCameraViewfinder()
        self.camvfindset = QCameraViewfinderSettings()
        self.cammode = self.cam.CaptureMode(0)
        self.camimgcap = QCameraImageCapture(self.cam)


    def iniCamera(self):
        print(self.caminfo.description())
        print(self.caminfo.availableCameras())

        for caminfo in QCameraInfo.availableCameras():
            print(caminfo.deviceName())

        if self.cam.isCaptureModeSupported(self.cammode):
            print("Capturemode supported")

    def startVid(self):

        self.camvfind.show()

        self.cam.setViewfinder(self.camvfind)

        self.cam.setCaptureMode(self.cammode)

        self.cam.start()

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    cam = Camera()
    cam.iniCamera()

    cam.startVid()

    sys.excepthook = except_hook
    sys.exit(app.exec_())