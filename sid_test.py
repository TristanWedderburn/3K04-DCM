# GUI FOR THE DCM CONTROLLER 
# KHANG, SID, AMITESH, DEREK
# 3k04 milestone1

from tkinter import *

# GUI

def Signup():
    global root
    global passwordE
    global usernameE

    root = Tk()
    roots.title('LABron Pacemaker')
    instruction = Label(root, text="Please sign up.")
    instruction.grid(row=0, column=0, sticky=E)

    username = Label(root, text="New Username: ")
    password = Label(roots, text="New Password: ")
    username.grid(row=1, column=0, sticky=W)
    password.grid(row=2, column=0, sticky=W)
    
    signupButton = Button(roots, text='Signup', command=FSSignup)
    signupButton.grid(columnspan=2, sticky=W)

    root.mainloop() # makes sure window doesn't close quickly

def FSSignup():
    with open(creds, 'w') as f:
        f.write(usernameE.get())
        f.write('\n')
        f.write(passwordE.get())
        f.close()
    
    roots.destroy()
    #Login()

# def Login():
