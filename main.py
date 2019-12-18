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
        self.setWindowTitle("Imagelator")
        self.setStyleSheet("background-color: white;")

        lang = ['한국어', '영어', '중국어 간체', '중국어 번체', '스페인어', '프랑스어', '베트남어', '태국어', '인도네시아어']

        self.original = QLabel("Text to Translate")
        self.result = QLabel("Result")

        self.changeButton = QPushButton("Change(F1)")
        self.changeButton.setStyleSheet("border: 1px solid #D0D3D1")#버튼 테두리 색 변경
        self.openButton = QPushButton("File Open(F2)") #파일 선택창을 띄우는 버튼
        self.openButton.setStyleSheet("border: 1px solid #D0D3D1")
        self.language = QComboBox()
        self.language.setStyleSheet("border: 1px solid #D0D3D1")
        self.clearButton = QPushButton("Clear(F3)")
        self.clearButton.setStyleSheet("border: 1px solid #D0D3D1")
        self.transButton = QPushButton("Translate(F4)")


        self.changeButton.clicked.connect(self.ButtonClicked)
        self.changeButton.setShortcut("F1")# f1을 누르면 change 작동 하도록 단축키 설정

        self.openButton.clicked.connect(self.ButtonClicked)
        self.openButton.setShortcut("F2")  # f4를 누르면 파일 열기 창 실행

        self.clearButton.clicked.connect(self.ButtonClicked)
        self.clearButton.setShortcut("F3")# f3를 누르면 모두 지우기

        self.transButton.clicked.connect(self.ButtonClicked)
        self.transButton.setShortcut("F4")  # f2를 누르면 번역

        self.origin = QTextEdit("", self)
        self.trans = QTextEdit("", self)

        #텍스트창 색 변경
        self.origin.setStyleSheet("border: 2px solid #89fa7d;")
        self.trans.setStyleSheet("border: 2px solid #89fa7d;")
        self.transButton.setStyleSheet("""background:solid #59FF7A;
                                          border: 2px solid #59FF7A;
                                          color : white;""")
        #입력된 글자가 변경되면 작동
        self.origin.textChanged.connect(self.textChanged)
        self.trans.textChanged.connect(self.textChanged)

        for lan in lang: # 언어의 키값을 combo 에 담음
            self.language.addItem(lan)

        hlayout = QHBoxLayout()
        buttonlayout = QVBoxLayout()
        textlayout = QVBoxLayout()

        buttonlayout.addWidget(self.language)
        buttonlayout.addWidget(self.changeButton)
        buttonlayout.addWidget(self.openButton)
        buttonlayout.addWidget(self.clearButton)
        buttonlayout.addWidget(self.transButton)

        textlayout.addWidget(self.original)
        textlayout.addWidget(self.origin)
        textlayout.addWidget(self.result)
        textlayout.addWidget(self.trans)
        hlayout.addLayout(textlayout)
        hlayout.addLayout(buttonlayout)

        self.setLayout(hlayout)
        self.show()

    # 사진의 경로를 얻어오는 버튼
    def ButtonClicked(self):
        button = self.sender()
        if button.text() == "File Open(F2)":
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
        elif button.text() == "Translate(F4)":
            if self.origin.toPlainText() != '':
                # 같은 언어 번역 시도시 발생하는 오류 제거
                try:
                    translator = DetectTranslator(self.language.currentText())
                    self.trans.setText(translator.translateText(self.origin.toPlainText()))
                except:
                    self.trans.setText("failed!"+self.origin.toPlainText())
            else:
                self.trans.setText("입력받은 문자가 없습니다!")

        elif button.text() == "Clear(F3)":
            self.origin.clear()
            self.trans.clear()

        elif button.text() == "Change(F1)":
            save = self.origin.toPlainText()
            self.origin.setText(self.trans.toPlainText())
            self.trans.setText(save)

    # esc 입력받으면 창을 종료
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
            try:
                self.pix.keyPressEvent(e)
            except:
                pass

    # 현재 입력된 글자수를 세줌
    def textChanged(self):
        self.original.setText("Text to Translate  " + str(len(self.origin.toPlainText())) + "/" +"5000")
        self.result.setText("Result  " + str(len(self.trans.toPlainText())) + "/" + "5000")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
