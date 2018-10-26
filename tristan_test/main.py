from checkComm import *
from getRef import *
from loginUser import *
from login import *
from register import *
from registerUser import  *
           
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
    if checkComm() == True:
        Label(text = "Device is IS communicating with the DCM",fg = "green").pack()
    elif checkComm() == False:
        Label(text = "Device is NOT communicating with the DCM",fg ="red").pack()
    
    screen.mainloop()

main_screen()
