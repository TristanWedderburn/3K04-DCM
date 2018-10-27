from Tkinter import *

def register():
    global register_screen
    register_screen = Toplevel(screen) # means creates a new empty screen  
    register_screen.title("Register")
    register_screen.geometry("300x300")# window size size
    global username
    global password
    global username_entry
    global password_entry 
    username = StringVar() #must be string
    password = StringVar() #must be string

    Label(register_screen,text = "Please Enter details below: ").pack()
    Label(register_screen,text = "").pack()
    Label(register_screen,text = "Username *").pack() # intialize which screen you want text to show up
    username_entry = Entry(register_screen,textvariable = username)
    username_entry.pack()#entry is a textbox
    Label(register_screen,text = "Password *").pack()
    password_entry = Entry(register_screen,textvariable = password)
    password_entry.pack()# whatever text is entered in the entry is stored in variable password
    Label(register_screen,text = "").pack()
    Button(register_screen, text = "Regsiter",width ="10", height ="1",command = Register_User).pack()