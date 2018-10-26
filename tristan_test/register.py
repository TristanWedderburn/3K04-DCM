from tkinter import *

def register():
    global screen1
    screen1 = Toplevel(screen) # means creates a new empty screen  
    screen1.title("Register")
    screen1.geometry("300x300")# window size size
    global username
    global password
    global username_entry
    global password_entry 
    username = StringVar() #must be string
    password = StringVar() #must be string

    Label(screen1,text = "Please Enter details below: ").pack()
    Label(screen1,text = "").pack()
    Label(screen1,text = "Username *").pack() # intialize which screen you want text to show up
    username_entry = Entry(screen1,textvariable = username)
    username_entry.pack()#entry is a textbox
    Label(screen1,text = "Password *").pack()
    password_entry = Entry(screen1,textvariable = password)
    password_entry.pack()# whatever text is entered in the entry is stored in variable password
    Label(screen1,text = "").pack()
    Button(screen1, text = "Regsiter",width ="10", height ="1",command = Register_User).pack()