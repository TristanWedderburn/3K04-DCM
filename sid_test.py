# GUI FOR THE DCM CONTROLLER 
# KHANG, SID, AMITESH, DEREK
# 3k04 milestone1

from tkinter import *
from tkinter import ttk

# GUI

gui = Tk()
gui.geometry("275x120")

gui.title("LABron Pacemaker")

ref={} # creates an empty dictionary

# Create new account

def newUser(us,pw):
    if len(ref) >= 10: 
        i=Label(gui,text='Error only 10 users allowed').grid(row=5,column=0)
        print("Error only 10 users allowed")
    else:
        ref[us] = pw # adds new key--value pair into the dictonary 
        j=Label(gui,text='New account created').grid(row=5,column=0)
        print("New account created")

# Login

def login(us,pw):
    for i in len(ref):
        if us == ref[i] and pw1 == pword:
            i=Label(gui,text='Login success').grid(row=5,column=0)
            print("Login success")
        else:
            j=Label(gui,text='Login failed').grid(row=5,column=0)
            print("Wrong password")

# Layout

uname = Label(gui ,text="username").grid(row=1,column=0)
pword = Label(gui ,text="password").grid(row=2,column=0)
u_entry = Entry(gui).grid(row=1,column=1)
p_entry = Entry(gui,show="*").grid(row=2,column=1)
createButton = Button(gui,text="Create account",command=lambda : newUser(u_entry,p_entry)).grid(row=3,column=0)
loginButton = Button(gui,text="Login",command=lambda : login(u_entry,p_entry)).grid(row=4,column=0)

gui.mainloop() # displays GUI