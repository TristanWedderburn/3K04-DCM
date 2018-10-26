from Tkinter import *

def getRef():
    userPassRef={}
    f = open("user_info.txt","r")
    for line in f.readlines():
        loginInfo = line.split(" ")
        userPassRef[loginInfo[0]] = loginInfo[1].strip("\n")

    f.close()
        
    return userPassRef