# -*- coding: utf-8 -*-

from pytesseract import *
from PIL import Image

class OCR:
    def __init__(self, dir):
        img = Image.open(dir)
        self.text = pytesseract.image_to_string(img, lang='kor+eng')

    def getString(self):
        sentence = self.text.split('\n')

        filtered = []

        for i in sentence:
            if len(i) != 0:
                filtered.append(i)

        return filtered