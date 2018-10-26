from tkinter import *

def Register_User():
    username_info = username.get()
    password_info = password.get()

    # insert details into a textfile to store


    with open("user_info.txt") as f:
        Num_Users = (len(f.readlines()))
        
    if (Num_Users == 10):
        print("Max Users Reached")

    else:
        
        file = open("user_info.txt","a")

       
        
        file.write(username_info +" "+password_info+"\n")
        file.close()

        username_entry.delete(0,END) #once information is stored in the textfile the data in the password and username textbox are deleted
        password_entry.delete(0,END)

        Label(screen1,text = "Registration Successful", fg = "green").pack()
    
    
def Register():
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
 
def Login():

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


def Login_User():
    
        userPassRef = getRef()
        if usernameInput.get() in userPassRef:
            if userPassRef[usernameInput.get()] == passwordInput.get():
                print("logging in user ok")
            else:
                print("wrong password")
        else:
            print("no user")
        

def getRef():
    userPassRef={}
    f = open("user_info.txt","r")
    for line in f.readlines():
        loginInfo = line.split(" ")
        userPassRef[loginInfo[0]] = loginInfo[1].strip("\n")

    f.close()
        
    return userPassRef

def checkCommunication():

    # this function will check when the dcm and python are communicating, At the moment we are not required to serially communicate therefore we will return false

    return False
        
           
def main_screen():

    global screen # need it available in other functions so we make it global
    
    screen = Tk();# main screen 
    screen.geometry("300x300") #window size
    screen.title("DCM")
    
    Label (text = "LABRON PACEMAKER 1.0",width = "300", bg = "light grey",font =("Calibri",13)).pack() #packs in rows and columns

    # creating register and login button
    Label(text = "").pack()
    Label(text = "").pack() 
    Label(text = "").pack() #leaves a blank line from the Labron pacemaker 1.0 text
    Button(text = "Login", height = "2", width = "10",command = Login).pack()
    Label(text = "").pack()
    Button(text= "Register", width = "10", height = "2",command = Register).pack()
    Label(text = "").pack()
    Label(text = "").pack()
    if checkCommunication() == True:
        Label(text = "Device is IS communicating with the DCM",fg = "green").pack()
    elif checkCommunication() == False:
        Label(text = "Device is NOT communicating with the DCM",fg ="red").pack()
    
    
    
    screen.mainloop()

main_screen()
