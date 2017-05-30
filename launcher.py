from project import *

loopFlag = 1
def printMenu():
    print("Hi! This is performance,exhibit search program ")
    print("######################Menu#####################")
    print("Data search: d")
    print("Area search: a")
    print("Quit: q")
    print("###############################################")


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
    menuKey = str(input("select Menu:"))
    launcherFunction(menuKey)


