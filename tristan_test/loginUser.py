from tkinter import *

ef loginUser():
    
        userPassRef = getRef()
        if usernameInput.get() in userPassRef:
            if userPassRef[usernameInput.get()] == passwordInput.get():
                print("logging in user ok")
            else:
                print("wrong password")
        else:
            print("no user")
        