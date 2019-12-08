#-*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from image import Image
from PyQt5.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 150)
        self.setWindowTitle("Test Title")

        self.openButton = QPushButton("File Open")
        self.openButton.clicked.connect(self.openButtonClicked)
        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.openButton)
        layout.addWidget(self.label)

        self.setLayout(layout)
        self.show()

    #Get File directory Button
    def openButtonClicked(self):
        fname = QFileDialog.getOpenFileName(self)
        self.label.setText(fname[0])
        self.dir = fname[0]
        self.pix = Image(self.dir)
        ocr = OCR(self.dir)
        self.sentences = ocr.getString()
        self.label.setText(self.sentences[0])
        
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
            try:
                self.pix.keyPressEvent(e)
            except:
                pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()

