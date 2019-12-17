import unittest

from DetectTranslator import DetectTranslator

class testDetectTranslator(unittest.TestCase):

    def setUp(self):
        self.kor = DetectTranslator("한국어")
        self.eng = DetectTranslator("영어")

    def testTranslateText(self):
        self.assertEqual(self.kor.translateText("apple"), "사과")
        self.assertEqual(self.eng.translateText("사과"), "apple")



