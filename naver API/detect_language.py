# 네이버 Papago 언어감지 API 예제
import os
import sys
import urllib.request
client_id = "qzJp_knRrRBfUxhE3Hly"  # 개발자센터에서 발급받은 client ID, 현승 네이버에 있음.
client_secret = "3DRB_k92uK"        # 개발자센터에서 발급받은 client secret.

encQuery = urllib.parse.quote("언어를 감지할 문장을 입력하세요")
data = "query=" + encQuery
url = "https://openapi.naver.com/v1/papago/detectLangs"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)