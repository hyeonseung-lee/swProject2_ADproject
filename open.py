#-*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from image import Image
from OCR import OCR
from DetectTranslator import DetectTranslator
from PyQt5.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 700, 700)
        self.setWindowTitle("Test Title")

        lang = ['한국어', '영어', '중국어 간체', '중국어 번체', '스페인어', '프랑스어', '베트남어', '태국어', '인도네시아어']

        original = QLabel("Text to Translate")
        result = QLabel("Result")

        self.changeButton = QPushButton("Change")
        self.openButton = QPushButton("File Open") #파일 선택창을 띄우는 버튼
        self.language = QComboBox()
        self.clearButton = QPushButton("Clear")
        self.transButton = QPushButton("Translate")

        self.changeButton.clicked.connect(self.ButtonClicked)
        self.transButton.clicked.connect(self.ButtonClicked)
        self.clearButton.clicked.connect(self.ButtonClicked)
        self.openButton.clicked.connect(self.ButtonClicked)
        self.origin = QTextEdit("", self)
        self.trans = QTextEdit("", self)

        for lan in lang: # 언어의 키값을 combo에 담음
            self.language.addItem(lan)

        hlayout = QHBoxLayout()
        buttonlayout = QVBoxLayout()
        mainlayout = QVBoxLayout()
        textlayout = QVBoxLayout()

        buttonlayout.addWidget(self.changeButton)
        buttonlayout.addWidget(self.openButton)
        buttonlayout.addWidget(self.language)
        buttonlayout.addWidget(self.clearButton)
        buttonlayout.addWidget(self.transButton)

        textlayout.addWidget(original)
        textlayout.addWidget(self.origin)
        textlayout.addWidget(result)
        textlayout.addWidget(self.trans)
        hlayout.addLayout(textlayout)
        hlayout.addLayout(buttonlayout)

        self.setLayout(hlayout)
        self.show()

    # 사진의 경로를 얻어오는 버튼
    def ButtonClicked(self):
        button = self.sender()
        if button.text() == "File Open":
            # 경로 선택창을 띄움
            fname = QFileDialog.getOpenFileName(self)
            # fname[0] == 사진의 경로
            try:
                self.dir = fname[0]
                # Image 클래스에 사진 경로를 입력, 이미지를 화면에 출력함
                self.pix = Image(self.dir)
                # OCR 클래스에 사진 경로를 입력, 이미지의 텍스트값을 리스트로 리턴
                ocr = OCR(self.dir)
                self.sentences = ocr.getString()
                for i in self.sentences:
                    self.origin.append(i)

            except:
                pass
        elif button.text() == "Translate":
            if self.origin.toPlainText() != '':
                #같은 언어 번역 시도시 발생하는 오류 제거
                try:
                    translator = DetectTranslator(self.language.currentText())
                    self.trans.setText(translator.translateText(self.origin.toPlainText()))
                except:
                    self.trans.setText(self.origin.toPlainText())
            else:
                self.trans.setText("입력받은 문자가 없습니다!")

        elif button.text() == "Clear":
            self.origin.clear()
            self.trans.clear()

        elif button.text() == "Change":
            save = self.origin.toPlainText()
            self.origin.setText(self.trans.toPlainText())
            self.trans.setText(save)

    #esc키 입력받으면 창을 종료
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

