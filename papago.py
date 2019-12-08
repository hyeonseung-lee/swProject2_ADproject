# 네이버 Papago NMT API 예제
import os
import sys
import json, pprint
import urllib.request   # 표준 라이브러리. 둘 다 다른곳에 요청하는 역할을 함.

client_id = "qzJp_knRrRBfUxhE3Hly"  # 개발자센터에서 발급받은 client ID, 현승 네이버에 있음.
client_secret = "3DRB_k92uK"        # 개발자센터에서 발급받은 client secret.

url = "https://openapi.naver.com/v1/papago/n2mt"

# 번여갈 언어와 내용에 대해
while True:
    text = input("번역할 내용을 입력하세요. : ")
    encText = urllib.parse.quote(text)

    srcLang = "ko"  # 번역 대상 언어를 한국어로 설정
    tarLang = "en"  # 번역 결과 언어를 영어로 설정
    data = "source={}&target={}&text=".format(srcLang, tarLang) + encText


    # 웹 요청
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)

    # 결과를 받아오는 부분
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))

    # 응답이 성공적일 때
    rescode = response.getcode()
    if(rescode==200):   # 성공
        response_body = response.read()
        data = response_body.decode('utf-8')
        data = json.loads(data) # to dictionary
        #pprint.pprint(data)     # data를 가시적으로 print

        trans_text = data['message']['result']['translatedText']

    else:   #실패
        print("Error Code:" + rescode)


    print("번역된 내용 : ", trans_text)