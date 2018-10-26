from tkinter import *

def login():

    global usernameInput
    global passwordInput
    
    usernameInput = StringVar()
    passwordInput =StringVar()
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x300")
    Label(screen2,text = "Please Enter Login info: ").pack()
    Label(screen2,text = "").pack()
    Label(screen2,text = "Username *").pack()
    userLogin = Entry(screen2,textvariable = usernameInput) 
    userLogin.pack()#entry is a textbox
    Label(screen2,text = "Password *").pack()
    passwordLogin = Entry(screen2,textvariable = passwordInput)
    passwordLogin.pack()
    Label(screen2,text = "").pack()
    Button(screen2, text = "Login",width ="10", height ="1",command = Login_User).pack()