# GUI FOR THE DCM CONTROLLER 
# KHANG, SID, AMITESH, DEREK
# 3k04 milestone1

from tkinter import *
import os

# creds = 'tempfile.temp'

# GUI

def Signup():
    global root
    global passwordE
    global usernameE

    root = Tk()
    root.title('LABron Pacemaker')
    instruction = Label(root, text="Please sign up.")
    instruction.grid(row=0, column=0, sticky=E)

    username = Label(root, text="New Username: ")
    password = Label(root, text="New Password: ")
    username.grid(row=1, column=0, sticky=W)
    password.grid(row=2, column=0, sticky=W)

    usernameE = Entry(root)
    passwordE = Entry(roots, show='*')
    
    signupButton = Button(root, text='Signup', command=FSSignup)
    signupButton.grid(columnspan=2, sticky=W)

    root.mainloop() # makes sure window doesn't close quickly

def FSSignup():
    with open(creds, 'w') as f:
        f.write(usernameE.get())
        f.write('\n')
        f.write(passwordE.get())
        f.close()
    
    root.destroy()
    Login()

def Login():
    global Name
    global Pass

    root1 = Tk()
    root1.title('Login')

    instruction = Label(root1, text='Please Login\n')
    instruction.grid(sticky=E)

    username = Label(root1, text='Username: ')
    password = Label(root1, text='Password: ')
    username.grid(row=1, sticky=W)
    password.grid(row=2, sticky=W)

    usernameEL = Entry(root1)
    passwordEL = Entry(root1, show='*')
    usernameEL.grid(row=1, column=1)
    passwordEL.grid(row=2, column=1)

    loginButton = Button(root1, text='Login', command=CheckLogin)
    loginButton.grid(columnspan=2, sticky=W)

    root1.mainloop()

def CheckLogin():
    with open(creds) as f:
        date = f.readlines()
        uname = data[0].rstrip()
        pword = data[1].rstrip()
    
    if Name.get() == uname and Pass == pword:
        r = Tk()
        r.title('Logged In')
        r.geometry('150x50')
        r.mainloop()
    
if os.path.isfile(creds):
    Login()
else:
    Signup()