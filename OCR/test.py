from DetectTranslator import *

text = "안녕 나는 실험대상이야."
target = "영어"


translator = DetectTranslator(target)

translated = translator.translateText(text)

print(translated)

