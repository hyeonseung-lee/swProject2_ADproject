import os
import sys
import json, pprint
import urllib.request

client_id = "qzJp_knRrRBfUxhE3Hly"  # client ID received from naver developer center.
client_secret = "3DRB_k92uK"        # client secret receiver from naver developer center.

trans_url = "https://openapi.naver.com/v1/papago/n2mt"
detect_url = "https://openapi.naver.com/v1/papago/detectLangs"

target_langCode = {"한국어" : "ko",
                   "영어" : "en",
                   "중국어 간체" : "zh-CN",
                   "중국어 번체" : "zh-TW",
                   "스페인어" : "es",
                   "프랑스어" : "fr",
                   "베트남어" : "vi",
                   "태국어" : "th",
                   "인도네시아어" : "id"}
# possible combinations : ko<->en, ko<->zh-CN, ko<->zh-TW, ko<->es, ko<->fr, ko<->vi, ko<->th, ko<->id, en<->ja, en<->fr

print("target languege list : ", list(target_langCode.keys()))  # show target list
target_Lang = input("PLZ select target language : ")            # input key
target_Lang = target_langCode[target_Lang]                      # set target code

while True:
    text = input("번역할 내용을 입력하세요. : ")


    ####################### detect language ##########################
    detect_encQuery = urllib.parse.quote(text)
    detect_data = "query=" + detect_encQuery

    # request to WEB
    detect_request = urllib.request.Request(detect_url)
    detect_request.add_header("X-Naver-Client-Id", client_id)
    detect_request.add_header("X-Naver-Client-Secret", client_secret)

    # get result
    detect_response = urllib.request.urlopen(detect_request, data=detect_data.encode("utf-8"))

    # successful responds
    detect_rescode = detect_response.getcode()
    if (detect_rescode == 200):    # success
        response_body = detect_response.read()
        detect_data = response_body.decode('utf-8')
        detect_data = json.loads(detect_data)
        #print("This languege code : ", detect_data["langCode"])

    else:   # fail
        print("Error Code:" + detect_rescode)


    ####################### translaor #################################
    trans_encText = urllib.parse.quote(text)
    srcLang = detect_data["langCode"]  # setting source from language detector
    tarLang = target_Lang              # setting target language from user selected
    trans_data = "source={}&target={}&text=".format(srcLang, tarLang) + trans_encText


    # request to WEB
    trans_request = urllib.request.Request(trans_url)
    trans_request.add_header("X-Naver-Client-Id",client_id)
    trans_request.add_header("X-Naver-Client-Secret",client_secret)

    # get result
    trans_response = urllib.request.urlopen(trans_request, data=trans_data.encode("utf-8"))

    # successful responds
    trans_rescode = trans_response.getcode()
    if(trans_rescode==200):   # success
        trans_response_body = trans_response.read()
        trans_data = trans_response_body.decode('utf-8')
        trans_data = json.loads(trans_data) # to dictionary
        #pprint.pprint(data)     # data print at looks good

        trans_text = trans_data['message']['result']['translatedText']

    else:   # fail
        print("Error Code:" + trans_rescode)


    print("번역된 내용 : ", trans_text)