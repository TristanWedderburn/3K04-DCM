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

		frame = Frame(width=400, height=150)
		frame.pack()
		Label(self,text =" ").pack()
		Label(self, text="WELCOME TO THE",fg = "Gold1",font=("Calibri", 20)).pack()
		Label(self,text =" ").pack()
		Label(self, text="LABRON PACEMAKER",fg="medium purple",font=("Calibri", 25)) .pack()
		Label(self,text =" ").pack()
		page_one = Button(self, text="Log In",width ="13",height="3", command=lambda:controller.show_frame(PageOne))
		page_one.pack(padx=40, pady=40)
		page_two = Button(self, text="Register",width ="13",height="3", command=lambda:controller.show_frame(PageTwo))
		page_two.pack()

class PageOne(Frame):#login page
        def __init__(self, parent, controller):
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
                password_Entry = Entry(self,textvariable = passwordInput,show ="*").pack()
                Label(self, text=" ").pack()
                Label(self, text=" ").pack()
                returnToMain = Button(self, text="Main Menu", command=lambda:controller.show_frame(StartPage))
                Label(self, text=" ").pack()
                LoginCurrentUser = Button(self, text="Log In", command=lambda:self.Login_User(usernameInput.get(),passwordInput.get()))
                returnToMain.pack()
                LoginCurrentUser.pack()


        def getuser(self):
                return usernameInput

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
                                print("logging in user ok")
                               #how to open new screen
                                
                                
                        else:
                                print("wrong password")
                else:
                        print("no user")
                
 
        
        
                

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
                        Label(self,text = "Maximum Userlimit Reached", fg = "red").pack()
                        return
                else:
                        file = open("user_info.txt","a")
                        file.write(username_info +" "+password_info+"\n")
                        file.close()
                        Label(self,text = "Registration Successful", fg = "green").pack()
    


class PageThree(Frame):#postLoginScreen
        def __init__(self, parent, controller):
                Frame.__init__(self, parent)
           
                page_three = Label(self, text="Welcome User")
                OPTIONS = ["Jan","Feb","March","April","May"]
                variable = StringVar(self)
                variable.set(OPTIONS[0])
                w = OptionMenu(self, variable, *OPTIONS)
                w.pack()





app = App()
app.mainloop()
