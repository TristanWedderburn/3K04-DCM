from Tkinter import *
import tkMessageBox
import os

class App(Tk):
	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)

		#Setup Frame
		container = Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
                
		self.frames = {}
                
		for F in (StartPage, PageOne, PageTwo, PageThree):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self, context):
		frame = self.frames[context]
		frame.tkraise()

class StartPage(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		frame = Frame(width=500, height=250)
		frame.pack()
		Label(self,text =" ").pack()
		Label(self, text="WELCOME TO THE",fg = "Gold1",font=("Calibri", 20)).pack()
		Label(self,text =" ").pack()
		Label(self,text="LABRON PACEMAKER",fg="medium purple",font=("Calibri", 25)) .pack()
		Label(self,text =" ").pack()
		page_one = Button(self, text="Log In",width ="13",height="3", command=lambda:controller.show_frame(PageOne))
		page_one.pack(padx=40, pady=40)
		page_two = Button(self, text="Register",width ="13",height="3", command=lambda:controller.show_frame(PageTwo))
		page_two.pack()

class PageOne(Frame):#login page
        def __init__(self, parent, controller):
                self.controller = controller
                Frame.__init__(self, parent)
                usernameInput = StringVar()
                passwordInput = StringVar()
                global userDatabase = self.getRef()
                
                #all of the pssible parameters
                global parameters=['Lower Rate Limit','Upper Rate Limit','Maximum Sensor Rate','Fixed AV Delay',
                 'Dynamic AV Delay','Sensed AV Delay Offset','Atrial Amplitude','Ventricular Amplitude','Atrial Pulse Width','Ventricular Pusle Width',
                 'Atrial Sensitivity','Ventricular Sensitivity','VRP','ARP','PVARP','PVARP Extension','Hysteresis','Rate Smoothing','ATR Duration'
                 ,'ATR Fallback Mode','ATR Fallback Time','Activity Threshold','Reaction Time','Response Factor','Recovery Time']

                # string or array for data structure?

                #all of the possible mode codes
                #each mode is represented as an index in the parameters array
                global AAT=[1,1,0,0,0,0,1,0,1,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0]
                global VVT=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]

                #to finish the rest of the codes
                global AOO=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
                global AAI=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
                global VOO=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
                global VVI=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
                global VDD=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
                global DOO=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
                global DDI=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
                global DDD=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
                global AOOR=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
                global AAIR=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
                global VOOR=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
                global VVIR=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
                global VDDR=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
                global DOOR=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
                global DDIR=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
                global DDDR=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]

                Label(self, text=" ").pack()
                Label(self, text=" ").pack()
                Label(self, text="Please Enter Login Details").pack()
                Label(self, text=" ").pack()
                Label(self, text=" ").pack()
                Label(self, text="Username *").pack()
                username_Entry = Entry(self,textvariable = usernameInput)
                username_Entry.pack()
                Label(self, text="Password *").pack()
                Entry(self,textvariable = passwordInput,show ="*").pack()
                Label(self, text=" ").pack()
                Label(self, text=" ").pack()
                Button(self, text="Log In", command=lambda:self.Login_User(usernameInput.get(),passwordInput.get())).pack()
                Button(self, text="Main Menu", command=lambda:controller.show_frame(StartPage)).pack()

        def next_page(self,next):
                        self.controller.show_frame(next)

        def getRef(self):
                global userDatabase
                userDatabase = {}#if no users, return empty database
                if(not (os.stat("user_info.txt").st_size == 0)):#not empty
                        f = open("user_info.txt","r")

                        for line in f.readlines():
                                loginInfo = line.split(" ")
                                username = loginInfo[0]
                                password = loginInfo[1].strip("\n")
                                
                                self temp_parameters =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                                if(len(loginInfo)>2)):
                                        for i in range(2,len(loginInfo)-1):#initialize any parameters stored for the user
                                                paramters[i-3]=loginInfo[i]

                                userDatabase[username] =User(username, password, temp_parameters)
                        f.close()
                return userDatabase        
                
        def Login_User(self,usernameInput,passwordInput):
                if usernameInput in userDatabase:
                        print("keys")
                        print(userDatabase.keys())
                        print("password")
                        print(userDatabase[usernameInput].getPassword())
                        if userDatabase[usernameInput].getPassword() == passwordInput:
                                print("Logged in")
                                return self.next_page(PageThree)
                        else:
                                print("Incorrect password2")				
                                tkMessageBox.showwarning("Error","Invalid Credentials.")
                else:
                        print("Incorrect password1")				
                        tkMessageBox.showwarning("Error","Invalid Credentials.")

class User():
        def __init__(self,name,password, parameters=[]):
                self.name = name
                self.password = password
                self.parameters = parameters#each index stores the parameters of the modes as a string?

        def getName(self):
                return self.name

        def getPassword(self):
                return self.password
        
        def getParameters(self):
                return self.parameters#returns object

class PageTwo(Frame):#register
        def __init__(self, parent, controller):
                Frame.__init__(self, parent)

                self.controller = controller
 
                Label(self,text=" ").pack()
                username =StringVar()
                password = StringVar()
                Label(self, text="Please Enter Registration Details Below.\nUsername and Password must only contain characters from A-Z.").pack()
                Label(self,text=" ").pack()
                Label(self, text="Username *").pack()
                username_Entry = Entry(self,textvariable = username)
                username_Entry.pack()
                Label(self,text=" ").pack()
                Label(self, text="Password*").pack()
                password_Entry = Entry(self,textvariable = password)
                password_Entry.pack()
                Label(self,text=" ").pack()
                ReturnToMenu = Button(self, text="Main Menu", command=lambda:controller.show_frame(StartPage))
                ReturnToMenu.pack()
                Label(self,text=" ").pack()
                createNewUser = Button(self, text="Register Account", command= lambda: self.Register_User(username.get(),password.get()))
                createNewUser.pack()

        def Register_User(self,username,password):
                global userDatabase
                Login_User = username
                Login_Password = password
                # insert details into a textfile to store
                            
                with open("user_info.txt") as f:
                        NumberofUsers = (len(f.readlines()))
                        
                if (NumberofUser == 10):
                        tkMessageBox.showwarning("Error","Max User Limit Reached")
                        return
                else:
                        if(self.validReg(username, password)):
                                #check if that user is already in the database
                                if(username in userDatabase and userDatabase[username].getPassword()==password):
                                        #throw error message for invalid credentials
                                        tkMessageBox.showwarning("Error","User with that username already in database.")
                                else:
                                        file = open("user_info.txt","a")
                                         #fix the writing to the file
                                         #function to turn all of the parameters indices to string then write to file
                                        file.write(Login_User +" "+Login_Password+"\n")#add current user to the database file on next line
                                        file.close()
                                        userDatabase[username]= User(username,password)#create add user to the dictionary instance to reference for login
                                        self.controller.show_frame(PageOne)#return to login page after registration
                                        return
                                
                                # Label(self,text = "Success", fg = "green").pack()
                        else:
                                tkMessageBox.showwarning("Error","Invalid Credentials.")
                                return

        def validReg(self, username, password):#check if the entered username and password fit the registration requirements for allowed characters
                for char in username:
                        if not char.isdigit() and not char.isalpha():
                               tkMessageBox.showwarning("Error","Invalid Credentials.")
                               return False

                for char in password:
                        if not char.isdigit() and not char.isalpha():
                               tkMessageBox.showwarning("Error","Invalid Credentials.")
                               return False
                return True#if successful, returns valid

        #dictionary for each user with first index as password
                        


#needs work for back end to add to userDatabase dictionary                        
class PageThree(Frame):#postLoginScreen
        def __init__(self, parent, controller):
               Frame.__init__(self, parent)
               self.controller = controller
               #before we add the value to the string, we have to validate it based on if statements?
               #then add them all to a final string to update the parameter
               global dropVar
               dropVar =StringVar()
               p_pacingState =StringVar()#permanent
               p_pacingMode = StringVar()#selected mode
               p_hysteresis = StringVar()#true or false
               p_hysteresisInterval = StringVar()#between 200 and 500
               p_lowrateInterval =StringVar()#between 343 and 200
               p_vPaceAmp = StringVar()#between 500 and 7000
               p_vPaceWidth = StringVar()#between 0.1 and 1.9
               p_vVRP = StringVar()#between 150-500

               def checkComm(self):
                       return False

               Label(self, text=" ").grid(row=0, column=0)
               Label(self, text="Parameters",font=("Calibri",15)).grid(row=0, column=0,pady=20)
               Label(self, text="p_pacingMode").grid(row=1, column=0)
               Label(self, text="PERMANENT").grid(row=1, column=1)
               
               Label(self, text="p_pacingState").grid(row=2, column=0)
               #VOO = index 0, AOO = index 1 VVI = index 2, AII = index 3 in parameters array in user dictionary
               dropVar.set('VOO') #default choice
               dropVar.trace('r', self.changeMode)
        #        self.changeMode(self.dropVar.get())
               OptionMenu(self,dropVar,'VOO','AOO','VVI','AAI').grid(column=1,row=2)

               Label(self, text="p_hysteresis").grid(row=3, column=0)
               Entry(self,textvariable = p_hysteresis).grid(row=3, column=1)
               Label(self, text="p_hysteresisInterval").grid(row=4, column=0)
               Entry(self,textvariable = p_hysteresisInterval).grid(row=4, column=1)
               Label(self, text="p_lowrateInterval").grid(row=5, column=0)
               Entry(self,textvariable = p_lowrateInterval).grid(row=5, column=1)
               Label(self, text="p_vPaceAmp").grid(row=6, column=0)
               Entry(self,textvariable = p_vPaceAmp).grid(row=6, column=1)
               Label(self, text="p_vPaceWidth").grid(row=7, column=0)
               Entry(self,textvariable = p_vPaceWidth).grid(row=7, column=1)
               Label(self, text="p_vVRP").grid(row=8, column=0)
               Entry(self,textvariable = p_vVRP).grid(row=8, column=1)

               Button(self, text="Update Parameters", command= lambda: self.updateParameters(p_pacingMode.get(), p_pacingState.get(),p_hysteresis.get(),p_hysteresisInterval.get(),p_lowrateInterval.get(),p_vPaceAmp.get(),p_vPaceWidth.get(),p_vVRP.get())).grid(row=9,column=1)
               
               
               if checkComm(self) == True:
                       Label(self,text = "Device is IS communicating with the DCM").grid(row=10, column=0,pady=20)
                       Label(self,text ="o",fg = "green").grid(row=10, column=1,pady=20)
               elif checkComm(self) == False:
                       Label(self,text = "Device is NOT communicating with the DCM").grid(row=10, column=0,pady=20)
                       Label(self,text ="o",fg = "red").grid(row=10, column=1,pady=20)
                
               Button(self, text="Log Out", command= lambda: self.controller.show_frame(PageOne)).grid(row=13,column=1)

        def changeMode(*args):
                mode = dropVar.get()
                if(mode=='VOO'):#if on the current page
                       print('no change')
                else:#changed the mode to a different page
                        print('changed mode')
                        # self.controller.show_frame(mode)

#update function so that the update adds to the dictionary then back to the file? or from the file then reinitialized to the dictionary
def updateParameters(self, state, string):#take string based on all of the values of the parameters
        #dictionary for the mode for index of each mode based on the string
        #each value separated by commas
               
               #update userDatabase dictonary first
               
               file = open("paramters_info.txt","w")
               file.writelines(["p_pacingMode"+" "+p_pacingMode+'\n',
                                "p_pacingState"+" "+p_pacingState+'\n'
                                "p_hysteresis"+" "+p_hysteresis+'\n'
                                "p_hysteresisInterval"+" "+p_hysteresisInterval+'\n'
                                "p_lowrateInterval"+" "+p_lowrateInterval+'\n'
                                "p_vPaceAmp"+" "+p_vPaceAmp+'\n'
                                "p_vPaceWidth"+" "+p_vPaceWidth+'\n'
                                "p_vVRP"+" "+p_vVRP+'\n'])
               
               file.close()
       
               win = Tk()
               win.geometry('150x150')
               win.title("Updated Paramters")
               Label(win, text="Paramters Updated",font =("Calibri",15),fg="green").grid(row=15,column=5)
               
app = App()
app.mainloop()
