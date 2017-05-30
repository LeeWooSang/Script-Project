from project import *

loopFlag = 1
def printMenu():
    print("공연/전시 검색 서비스")
    print("======================Menu=====================")
    print("기간별 공연/전시 검색 : d")
    print("지역별 공연/전시 검색 : a")
    print("프로그램 종료 : q")
    print("===============================================")


def launcherFunction(menu):
    if menu == 'd':
        Date_Showing_Parsing()
    elif menu == 'a':
        Area_Showing_Parsing()
    elif menu == 'q':
        Quit()
        print("Good bye!")


def Quit():
    global loopFlag
    loopFlag = 0

while(loopFlag > 0):
    printMenu()
    menuKey = str(input("메뉴를 선택해주세요 : "))
    launcherFunction(menuKey)


