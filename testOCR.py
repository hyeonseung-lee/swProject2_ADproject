import unittest

from OCR import OCR

class testOCR(unittest.TestCase):

    def setUp(self):
        self.py = OCR("/home/jung/바탕화면/result.png")

    def testgetString(self):
        text = self.py.getString()
        self.assertTrue(len(text) > 0)
        

