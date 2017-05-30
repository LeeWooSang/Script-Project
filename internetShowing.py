from http.client import  HTTPConnection
from http.server import  BaseHTTPRequestHandler,HTTPServer
import urllib.request

key = 'ivgVuV9%2BpIPYl3Gq%2F%2FsGzij9zmnKb3%2BAjlFJ%2BE61piuUo%2FgfsdUCHc7dZaUMFwIfwbXy%2FqpMYMj2VSxM7RSD8Q%3D%3D'

def Date_Showing_Parsing():
    time1 = str(input("언제부터 : "))
    time2 = str(input("언제까지 : "))

    global key

    url = 'http://www.culture.go.kr/openapi/rest/publicperformancedisplays/period?'
    new_url = url + 'from=' + time1 + '&to=' + time2 + '&cPage=1&rows=10&gpsxfrom=&gpsyfrom=&gpsxto=&gpsyto=&keyword=&sortStdr=1' + '&serviceKey=' + key

    data=urllib.request.urlopen(new_url).read()
    d=str(data,"utf-8")

    from xml.etree import ElementTree
    tree = ElementTree.fromstring(d)
    #print(d)

    itemElements = tree.getiterator("perforList")  # return list type
    #print(itemElements)
    for perforList in itemElements:
        title = perforList.find("title").text
        startDate = perforList.find("startDate").text
        endDate = perforList.find("endDate").text
        place = perforList.find("place").text
        realmName = perforList.find("realmName").text
        area = perforList.find("area").text

        print("=========================================")
        print("제목 : ", title)
        print("장르 : ", realmName)
        print("시작일 : ", startDate)
        print("마감일 : ", endDate)
        print("장소 : ", place)
        print("지역 : ", area)
        print("=========================================\n")

        #if len(title) > 0:
           # return {"제목": title.text, "장르": realName.text, "시작일": startDate.text, "마감일": endDate.text, "장소":place.text, "지역":area.text}

def Area_Showing_Parsing():
    sido = str(input("시/도 입력 : "))
    gugun = str(input("군/구 입력 : "))

    global key

    url = 'http://www.culture.go.kr/openapi/rest/publicperformancedisplays/area?'
    new_url = url + 'sido=' + sido + '&gugun=' + gugun + '&from=20170101&to=20171231&cPage=1&rows=10&gpsxfrom=&gpsyfrom=&gpsxto=&gpsyto=&keyword=&sortStdr=1' + '&serviceKey=' + key

    data=urllib.request.urlopen(new_url).read()
    d=str(data,"utf-8")

    from xml.etree import ElementTree
    tree = ElementTree.fromstring(d)
    #print(d)

    itemElements = tree.getiterator("perforList")  # return list type
   #print(itemElements)
    for perforList in itemElements:
        title = perforList.find("title").text
        startDate = perforList.find("startDate").text
        endDate = perforList.find("endDate").text
        place = perforList.find("place").text
        realName = perforList.find("realmName").text
        area = perforList.find("area").text

        print(title)
        print(realName)
        print(startDate)
        print(endDate)
        print(sido)
        print(gugun)
        print(place)

       # if len(title) > 0:
       #     return {"제목": title.text, "장르": realName.text, "시작일": startDate.text, "마감일": endDate.text, "시/도":sido.text, "군/구":gugun.text, "장소": place.text}

