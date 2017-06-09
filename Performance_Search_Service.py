from tkinter import font
from tkinter import *
import urllib.request
import urllib
from PIL import Image,ImageTk
from io import BytesIO
import tkinter.messagebox

key = 'ivgVuV9%2BpIPYl3Gq%2F%2FsGzij9zmnKb3%2BAjlFJ%2BE61piuUo%2FgfsdUCHc7dZaUMFwIfwbXy%2FqpMYMj2VSxM7RSD8Q%3D%3D'
window = Tk()
window.geometry("720x600")
window.title("Performance Search")


def Search_date():
    global key

    time1 = str(e1.get())
    time2 = str(e2.get())
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
        seq = perforList.find("seq").text

        RenderText.insert(INSERT, "=========================================\n")
        RenderText.insert(INSERT, "제목 : ")
        RenderText.insert(INSERT, title)
        RenderText.insert(INSERT, '\n')
        RenderText.insert(INSERT, "장르 : ")
        RenderText.insert(INSERT, realmName)
        RenderText.insert(INSERT, '\n')
        #RenderText.insert(INSERT, "시작일 : ")
        #RenderText.insert(INSERT, startDate)
        #RenderText.insert(INSERT, '\n')
        #RenderText.insert(INSERT, "마감일 : ")
        #RenderText.insert(INSERT, endDate)
        #RenderText.insert(INSERT, '\n')
        #RenderText.insert(INSERT, "장소 : ")
        #RenderText.insert(INSERT, place)
        #RenderText.insert(INSERT, '\n')
        RenderText.insert(INSERT, "일련번호: ")
        RenderText.insert(INSERT, seq)
        RenderText.insert(INSERT, '\n')
        #RenderText.insert(INSERT,"=========================================\n")


def Search_Area():
    sido = str(e3.get())
    hangul_sido = urllib.parse.quote(sido)
    gugun = str(e4.get())
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

        RenderText.insert(INSERT, "=========================================\n")
        RenderText.insert(INSERT, "제목 : ")
        RenderText.insert(INSERT, title)
        RenderText.insert(INSERT, '\n')
        RenderText.insert(INSERT, "장르 : ")
        RenderText.insert(INSERT, realmName)
        RenderText.insert(INSERT, '\n')
        #RenderText.insert(INSERT, "시작일 : ")
        #RenderText.insert(INSERT, startDate)
        #RenderText.insert(INSERT, '\n')
        #RenderText.insert(INSERT, "마감일 : ")
        #RenderText.insert(INSERT, endDate)
        #RenderText.insert(INSERT, '\n')
        #RenderText.insert(INSERT, "장소 : ")
        #RenderText.insert(INSERT, place)
        #RenderText.insert(INSERT, '\n')
        RenderText.insert(INSERT, "일련번호: ")
        RenderText.insert(INSERT, seq)
        RenderText.insert(INSERT, '\n')
        #RenderText.insert(INSERT, "=========================================\n")

def Search_specific_data():
    global key

    seq_num = str(e5.get())
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

        image_url = image
        with urllib.request.urlopen(image_url) as u:
            raw_data = u.read()

        im = Image.open(BytesIO(raw_data))
        post_image = ImageTk.PhotoImage(im)

        poster.configure(image=post_image)
        poster.image = post_image


        #RenderText.insert(INSERT, "=========================================\n")
        SpecificData.insert(INSERT, "제목 : ")
        SpecificData.insert(INSERT, title)
        SpecificData.insert(INSERT, '\n')
        #SpecificData.insert(INSERT, "장르 : ")
        #SpecificData.insert(INSERT, realmName)
        #SpecificData.insert(INSERT, '\n')
        SpecificData.insert(INSERT, "시작일 : ")
        SpecificData.insert(INSERT, startDate)
        SpecificData.insert(INSERT, '\n')
        SpecificData.insert(INSERT, "마감일 : ")
        SpecificData.insert(INSERT, endDate)
        SpecificData.insert(INSERT, '\n')
        SpecificData.insert(INSERT, "장소 : ")
        SpecificData.insert(INSERT, place)
        SpecificData.insert(INSERT, '\n')
        #SpecificData.insert(INSERT, "상세 정보: ")
        #RenderText.insert(INSERT, content)
        #RenderText.insert(INSERT, '\n')
        SpecificData.insert(INSERT, "금액: ")
        SpecificData.insert(INSERT, price)
        SpecificData.insert(INSERT, '\n')
        SpecificData.insert(INSERT, "구매 주소: ")
        SpecificData.insert(INSERT, buying_url)
        SpecificData.insert(INSERT, '\n')
        SpecificData.insert(INSERT, "연락처: ")
        SpecificData.insert(INSERT, phone)
        #RenderText.insert(INSERT, '\n')
        #RenderText.insert(INSERT, "=========================================\n")


def SearchButtonAction():
    RenderText.configure(state ='normal')
    RenderText.delete(0.0, END)
    Search_date()
    RenderText.configure(state='disabled')

def SearchButtonAction2():
    RenderText.configure(state ='normal')
    RenderText.delete(0.0, END)
    Search_Area()
    RenderText.configure(state='disabled')

def SearchButtonAction3():
    SpecificData.configure(state ='normal')
    SpecificData.delete(0.0, END)
    Search_specific_data()
    SpecificData.configure(state='disabled')

myfont = font.Font(window, size=25, weight = 'normal', family = 'Times')
Main = Label(window, fg = 'orange',font = myfont, text = '공연/전시 검색 서비스')
Main.pack()
Main.place(x=80, y=10)

#b1 = Button(window, text = 'Search', command=SearchButtonAction)
#b1.pack()
#b1.place(x=400, y=55)

b2 = Button(window, text = 'Search', command=SearchButtonAction2)
b2.pack()
b2.place(x=400, y=95)

b3 = Button(window, text = 'Search', command=SearchButtonAction3)
b3.pack()
b3.place(x=200, y=135)

l1 = Label(window, text = '언제부터')
l2 = Label(window, text = '언제까지')
l3 = Label(window, text = '시/도')
l4 = Label(window, text = '군/구')
l5 = Label(window, text = '일련번호')

l1.place(x=0, y=60)
l2.place(x=200, y=60)
l3.place(x=0, y=100)
l4.place(x=200, y=100)
l5.place(x=0, y=140)

#e1 = Entry(window)
#e2 = Entry(window)
e3 = Entry(window)
e4 = Entry(window)
e5 = Entry(window)

#e1.place(x=50, y=60)
#e2.place(x=250, y=60)
e3.place(x=50, y=100)
e4.place(x=250, y=100)
e5.place(x=50, y=140)

Month1scroll = Scrollbar(window)
Month1scroll.pack()
Month1scroll.place(x=75,y=45)
font1 = font.Font(size=12,weight='bold')
Month1 = Listbox(window,width=2,height=1,borderwidth=5,font=font1,yscrollcommand=Month1scroll.set)
Month1.insert(1,'01')
Month1.insert(2,'02')
Month1.insert(3,'03')
Month1.insert(4,'04')
Month1.insert(5,'05')
Month1.insert(6,'06')
Month1.insert(7,'07')
Month1.insert(8,'08')
Month1.insert(9,'09')
Month1.insert(10,'10')
Month1.insert(12,'11')
Month1.insert(12,'12')
Month1.pack()
Month1.place(x=50,y=55)
Month1scroll.config(command=Month1.yview)


poster = Label(window, image=None, height=300, width=200)
poster.pack()
poster.place(x=450, y=10)

RenderTextScrollbar = Scrollbar(window)

RenderText = Text(window, width=50, height=30, borderwidth=10, relief='raised', yscrollcommand=RenderTextScrollbar.set)
RenderText.pack()
RenderText.place(x=10, y=170)
RenderTextScrollbar.config(command=RenderText.yview)
RenderTextScrollbar.pack(side=RIGHT,fill=BOTH)

RenderText.configure(state='disabled')

SpecificData = Text(window, width=35, height=20, borderwidth=12, relief='raised')
SpecificData.pack()
SpecificData.place(x=415, y=300)

SpecificData.configure(state='disabled')

window.mainloop()
