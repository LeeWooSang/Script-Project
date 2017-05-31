from project import *

loopFlag = 1
def printMenu():
    print("Hi! This is performance,exhibit search program ")
    print("######################Menu#####################")
    print("기간별 검색: d")
    print("장소별 검색: a")
    print("상세정보 검색: s")
    print("Quit: q")
    print("###############################################")


def launcherFunction(menu):
    if menu == 'd':
        Date_Showing_Parsing()
    elif menu == 'a':
        Area_Showing_Parsing()
    elif menu == 's':
        specific_data()
    elif menu == 'q':
        Quit()
        print("Good bye!")


def Quit():
    global loopFlag
    loopFlag = 0

while(loopFlag > 0):
    printMenu()
    menuKey = str(input("원하는 검색을 선택하세요:"))
    launcherFunction(menuKey)


