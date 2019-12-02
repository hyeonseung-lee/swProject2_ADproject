import sys
from PyQt5.QtWidgets import  *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class Image(QMainWindow):
    def __init__(self, data): #data = 파일의 경로
        super().__init__()

        self.dir = data
        self.initUI()
        self.setWindowTitle('Image')


    def initUI(self):
        self.lbl = QLabel(self)
        pixmap = QPixmap(self.dir) #파일 경로에 해당하는 이미지를 불러옴
        height, width= pixmap.height(), pixmap.width() #이미지의 크기를 구함
        self.setGeometry(800- width, 200, width, height)
        self.lbl.resize(width, height)
        self.lbl.setPixmap(QPixmap(pixmap))

        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
