import urllib.request
import urllib

from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer


key = 'ivgVuV9%2BpIPYl3Gq%2F%2FsGzij9zmnKb3%2BAjlFJ%2BE61piuUo%2FgfsdUCHc7dZaUMFwIfwbXy%2FqpMYMj2VSxM7RSD8Q%3D%3D'

def specific_data():
    global key

    seq_num = str(input("일련번호를 입력하세요: "))
    url = 'http://www.culture.go.kr/openapi/rest/publicperformancedisplays/d/?'
    new_url = url + "seq=" + seq_num +"&serviceKey=" + key

    data = urllib.request.urlopen(new_url).read()
    d = str(data.decode('utf-8'))

    from xml.etree import ElementTree
    tree = ElementTree.fromstring(d)

    itemElements = tree.getiterator("perforInfo")
    for perforList in itemElements:
        title = perforList.find("title").text
        startDate = perforList.find("startDate").text
        endDate = perforList.find("endDate").text
        place = perforList.find("place").text
        realmName = perforList.find("realmName").text
        price = perforList.find("price").text
        content = perforList.find("contents1").text
        buying_url = perforList.find("url").text
        phone = perforList.find("phone").text
        image = perforList.find("imgUrl").text
        area = perforList.find("area").text

        print("=========================================")
        print("제목 : ", title)
        print("장르 : ", realmName)
        print("시작일 : ", startDate)
        print("마감일 : ", endDate)
        print("장소 : ", place)
        print("지역 : ", area)
        print("구매 주소: ", buying_url)
        print("전화번호: ", phone)
        print("포스터: ", image)
        print("상세 내용: ", content)
        print("=========================================\n")



def Date_Showing_Parsing():
    global key

    time1 = str(input("언제부터 : "))
    time2 = str(input("언제까지 : "))
    url = 'http://www.culture.go.kr/openapi/rest/publicperformancedisplays/period?'
    new_url = url + 'from=' + time1 + '&to=' + time2 + '&cPage=1&rows=10&gpsxfrom=&gpsyfrom=&gpsxto=&gpsyto=&keyword=&sortStdr=1' + '&serviceKey=' + key

    data=urllib.request.urlopen(new_url).read()
    d=str(data.decode('utf-8'))

    from xml.etree import ElementTree
    tree = ElementTree.fromstring(d)

    itemElements = tree.getiterator("perforList")  # return list type
    #print(itemElements)
    for perforList in itemElements:
        title = perforList.find("title").text
        startDate = perforList.find("startDate").text
        endDate = perforList.find("endDate").text
        place = perforList.find("place").text
        realmName = perforList.find("realmName").text
        area = perforList.find("area").text
        seq = perforList.find("seq").text

        print("=========================================")
        print("제목 : ", title)
        print("장르 : ", realmName)
        print("시작일 : ", startDate)
        print("마감일 : ", endDate)
        print("장소 : ", place)
        print("지역 : ", area)
        print("일련번호: ", seq)
        print("=========================================\n")


def Area_Showing_Parsing():
    sido = str(input("시/도 입력 : "))
    hangul_sido = urllib.parse.quote(sido)
    gugun = str(input("군/구 입력 : "))
    hangul_gugun = urllib.parse.quote(gugun)

    global key

    url = 'http://www.culture.go.kr/openapi/rest/publicperformancedisplays/area?'
    new_url = url + 'sido=' + hangul_sido + '&gugun=' + hangul_gugun + '&from=20170101&to=20170431&cPage=1&rows=10&gpsxfrom=&gpsyfrom=&gpsxto=&gpsyto=&keyword=&sortStdr=1' + '&serviceKey=' + key

    data=urllib.request.urlopen(new_url).read()
    d=str(data.decode('utf-8'))

    from xml.etree import ElementTree
    tree = ElementTree.fromstring(d)
    #print(d)

    itemElements = tree.getiterator("perforList")  # return list type
    print(itemElements)
    for perforList in itemElements:
        title = perforList.find("title").text
        startDate = perforList.find("startDate").text
        endDate = perforList.find("endDate").text
        place = perforList.find("place").text
        realmName = perforList.find("realmName").text
        seq = perforList.find("seq").text

        print("=========================================")
        print("제목 : ", title)
        print("장르 : ", realmName)
        print("시작일 : ", startDate)
        print("마감일 : ", endDate)
        print("장소 : ", place)
        print("일련번호: ", seq)
        print("=========================================\n")