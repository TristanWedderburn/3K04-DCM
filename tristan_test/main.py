import Tkinter
from checkComm import *
from getRef import *
from loginUser import *
from login import *
from register import *
from registerUser import  *
           
# def main_screen():

#  # need it available in other functions so we make it global
    
#     screen = Tkinter.Tk();# main screen 
#     screen.geometry("300x300") #window size
#     screen.title("DCM")
    
#     Label(text = "PACEMAKER 1.0",width = "300", bg = "light grey",font =("Calibri",13)).grid(row=1) #packs in rows and columns

#     # # creating register and login button

#     Button(text = "Login", height = "2", width = "10").grid(row=2)
#     Button(text= "Register", width = "10", height = "2").grid(row=3)
#     # Button(text="Exit", command=quit).grid(row=3)

#     # if checkComm() == True:
#     #     Label(text = "Device is IS communicating with the DCM",fg = "green").pack()
#     # elif checkComm() == False:
#     #     Label(text = "Device is NOT communicating with the DCM",fg ="red").pack()
    
#     screen.mainloop()

# main_screen()

class StartPage(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

        parent.title("PACEMAKER 1.0")

        label = Label(master, text="Welcome to the PACEMAKER 1.0")
        label.grid(row=0, column=0)

        self.login_button = Button(master, text="Login")
        self.login_button.grid(row=1, column=0)

        self.register_button = Button(master, text="Register")
        self.register_button.grid(row=2, column=0)

        self.exit_button = Button(master, text="Exit", command=master.quit)
        self.exit_button.grid(row=3, column=0)

        # if checkComm() == True:
        Label(text = "Device is IS communicating with the DCM").grid(row=4, column=0)
        Label(text ="o",fg = "green").grid(row=4, column=1)
        # elif checkComm() == False:
        Label(text = "Device is NOT communicating with the DCM").grid(row=5, column=0)
        Label(text ="o",fg = "red").grid(row=5, column=1)

        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)
        self.login_button.columnconfigure(0, weight=1)
        self.register_button.columnconfigure(0, weight=1)
        self.exit_button.columnconfigure(0, weight=1)

# class main_screen:
#     def __init__(self, master):
#         self.master = master
#         master.title("PACEMAKER 1.0")

#         label = Label(master, text="Welcome to the PACEMAKER 1.0")
#         label.grid(row=0, column=0)

#         self.login_button = Button(master, text="Login")
#         self.login_button.grid(row=1, column=0)

#         self.register_button = Button(master, text="Register")
#         self.register_button.grid(row=2, column=0)

#         self.exit_button = Button(master, text="Exit", command=master.quit)
#         self.exit_button.grid(row=3, column=0)

#         # if checkComm() == True:
#         Label(text = "Device is IS communicating with the DCM").grid(row=4, column=0)
#         Label(text ="o",fg = "green").grid(row=4, column=1)
#         # elif checkComm() == False:
#         Label(text = "Device is NOT communicating with the DCM").grid(row=5, column=0)
#         Label(text ="o",fg = "red").grid(row=5, column=1)

#         master.columnconfigure(0, weight=1)
#         master.rowconfigure(0, weight=1)
#         self.login_button.columnconfigure(0, weight=1)
#         self.register_button.columnconfigure(0, weight=1)
#         self.exit_button.columnconfigure(0, weight=1)

# screen = Tk()
# screen.geometry("300x300")
# main_screen(screen)
# screen.mainloop()
