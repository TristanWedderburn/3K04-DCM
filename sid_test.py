# GUI FOR THE DCM CONTROLLER 
# KHANG, SID, AMITESH, DEREK
# 3k04 milestone1

from tkinter import *
from tkinter import ttk

# GUI

gui = Tk()
gui.geometry("400x400")

def login(us1,pw1,usr,pword):
    if us1 == usr and pw1 == pword:
        i=Label(gui,text='Login success').grid(row=6,column=0)
        print("Login success")
    else:
        j=Label(gui,text='Login failed').grid(row=6,column=0)
        print("Wrong password")

gui.title("LABron Pacemaker")

# Create Account Section
uname = Label(gui ,text="username").grid(row=0,column=0)
pword = Label(gui ,text="password").grid(row=1,column=0)
u_entry = Entry(gui).grid(row=0,column=1)
p_entry = Entry(gui,show="*").grid(row=1,column=1)
createButton = Button(gui,text="Create account").grid(row=2,column=0)

# Login Section
uname1 = Label(gui ,text="username").grid(row=3,column=0)
pword1 = Label(gui ,text="password").grid(row=4,column=0)
u_entry1 = Entry(gui).grid(row=3,column=1)
p_entry1 = Entry(gui,show="*").grid(row=4,column=1)
loginButton = Button(gui,text="Login",command=lambda : login(u_entry,p_entry,u_entry1,p_entry1)).grid(row=5,column=0)

gui.mainloop() # displays GUI