from tkinter import *

def registerUser():
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