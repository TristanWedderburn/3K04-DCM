from tkinter import *

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
                returnToMain = Button(self, text="Main Menu", command=lambda:controller.show_frame(StartPage))
                Label(self, text=" ").pack()
                LoginCurrentUser = Button(self, text="Log In", command=lambda:self.Login_User(usernameInput.get(),passwordInput.get()))
                                # return controller.show_frame(PostLoginScreen)
                returnToMain.pack()
                LoginCurrentUser.pack()
                # user = usernameInput
                  
        # def getuser(self):
        #         return user
        def next_page(self,next):
                        self.controller.show_frame(next)

        def getRef(self):
                userPassRef={}
                f = open("user_info.txt","r")
                for line in f.readlines():
                        loginInfo = line.split(" ")
                        userPassRef[loginInfo[0]] = loginInfo[1].strip("\n")
                f.close()
                return userPassRef

        def Login_User(self,usernameInput,passwordInput):
                userPassRef = self.getRef()
                if usernameInput in userPassRef:
                        if userPassRef[usernameInput] == passwordInput:
                                print("Logged in")
                                return self.next_page(PageThree)
                        else:
                                print("Incorrect password")				
                                noLogin = Tk()
                                noLogin.geometry('300x300')
                                noLogin.title("Wrong User/Pass")
                                Label(noLogin, text="Wrong User/Pass",font =("Calibri",15),fg="red").grid(row=15,column=5)

                else:

                        
                        print("Incorrect password")				
                        noLogin = Tk()
                        noLogin.geometry('300x300')
                        noLogin.title("No User")
                        Label(noLogin, text="No Such User, Please Register",font =("Calibri",15),fg="red").grid(row=15,column=5)
			   
                        
                        
class PageTwo(Frame):#register

        def __init__(self, parent, controller):
                Frame.__init__(self, parent)
                Label(self,text=" ").pack()
                username =StringVar()
                password = StringVar()
                Label(self, text="Please Enter Registeration Details Below").pack()
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
                
                username_info = username
                password_info = password
                # insert details into a textfile to store
                            
                with open("user_info.txt") as f:
                        Num_Users = (len(f.readlines()))
                        
                                
                if (Num_Users == 10):
                        
                        noRegister = Tk()
                        noRegister.geometry('300x300')
                        noRegister.title("Max Limit Reached")
                        Label(noRegister, text="Max Limit Reached",font =("Calibri",15),fg="red").grid(row=15,column=5)
                        return
                else:
                        file = open("user_info.txt","a")
                        file.write(username_info +" "+password_info+"\n")
                        file.close()
                        Label(self,text = "Registration Successful", fg = "green").pack()

class PageThree(Frame):#postLoginScreen
       def __init__(self, parent, controller):
               Frame.__init__(self, parent)

               p_pacingState =StringVar()
               p_pacingMode = StringVar()
               p_hysteresis = StringVar()
               p_hysteresisInterval = StringVar()
               p_lowrateInterval =StringVar()
               p_vPaceAmp = StringVar()
               p_vPaceWidth = StringVar()
               p_vVRP = StringVar()

               def checkComm(self):
                       return False

               Label(self, text=" ").grid(row=0, column=0)
               Label(self, text="Parameters",font=("Calibri",15)).grid(row=0, column=0,pady=20)
               Label(self, text="p_pacingMode").grid(row=1, column=0)
               optionList=["VOO","AOO","VVI","AAI"]
               self.dropVar=StringVar()
               self.dropVar.set("VOO") #default choice
               self.dropMenu = OptionMenu(self,self.dropVar,*optionList)
               self.dropMenu.grid(column=1,row=1)
               #Entry(self,textvariable = p_pacingState).grid(row=1, column=1)
               Label(self, text="p_pacingState").grid(row=2, column=0)
               Entry(self,textvariable = p_pacingMode).grid(row=2, column=1)
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
                       Label(self,text = "Device is NOT communicating with the DCM").grid(row=11, column=0,pady=20)
                       Label(self,text ="o",fg = "red").grid(row=11, column=1,pady=20)

       def updateParameters(self, p_pacingState, p_pacingMode,p_hysteresis,p_hysteresisInterval,p_lowrateInterval,p_vPaceAmp,p_vPaceWidth,p_vVRP):

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
