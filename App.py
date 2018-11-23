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

                global userDatabase
                userDatabase = {}

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

                global userDatabase

                global parameters

                parameters=['Lower Rate Limit','Upper Rate Limit','Maximum Sensor Rate',

                 'Atrial Amplitude','Ventricular Amplitude','Atrial Pulse Width','Ventricular Pusle Width',

                 'Atrial Sensitivity','Ventricular Sensitivity','VRP','ARP','PVARP','Hysteresis',
                'Rate Smoothing','Activity Threshold','Reaction Time','Response Factor','Recovery Time']

                global PacingModesList

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

                global userDatbase
                
                global outputData
                outputData = ""

                #initiaize all of the user object using the text file
                #initialize username and password

                if(not (os.stat("user_info.txt").st_size == 0)):#not empty

                        f = open("user_info.txt","r")

                        for line in f.readlines():
                                print('line')
                                print(line)

                                loginInfo = line.split(" ")
                                if(loginInfo[0]=="\n"):
                                        continue
                                print(loginInfo)
                                username = loginInfo[0]

                                password = loginInfo[1].strip("\n")

                                userDatabase[username]=User(username, password)#stores user in userDatabase
                                
                        f.close()
                        
                        f = open("parameters_info.txt","r")

                        for line in f.readlines():
                                user = line.split(',')
                                name=str(user[0])
                                userDatabase[name].parameters[user[1]] = user[2:20]
                                userDatabase[name].parameters[user[20]] = user[21:39]
                                #19 for each one
                                #name +19 =next one
                                userDatabase[name].parameters[user[39]] = user[40:58]
                                userDatabase[name].parameters[user[58]] = user[59:77]
                                userDatabase[name].parameters[user[77]] = user[78:96]
                                userDatabase[name].parameters[user[96]] = user[97:115]
                                userDatabase[name].parameters[user[115]] = user[116:134]
                                userDatabase[name].parameters[user[134]] = user[135:153]

                return userDatabase        

                

        def Login_User(self,usernameInput,passwordInput):

                userDatabase = self.getRef()

                if usernameInput in userDatabase:

                        if userDatabase[usernameInput].getPassword() == passwordInput:

                                global currentUser

                                currentUser = usernameInput

                                return self.next_page(PageThree)

                        else:			

                                tkMessageBox.showwarning("Error","Invalid Credentials.")

                else:				

                        tkMessageBox.showwarning("Error","Invalid Credentials.")



class User():

        def __init__(self,name,password,parameters={},outputData=''):

                self.name = name#name string
                
                self.password = password#password string

                # self.outputData = outputData#string of output data

                self.parameters = parameters#each index stores the parameters of the modes as a string?

        def getName(self):

                return self.name

        def getPassword(self):

                return self.password

        def getParameters(self):

                return self.parameters#returns object
        
        # def getOutputData(self):
        #         return self.outputData



class PageTwo(Frame):#register

        def __init__(self, parent, controller):

                Frame.__init__(self, parent)

                global userDatabase

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

                createNewUser = Button(self, text="Register Account", command=lambda: self.Register_User(username.get(),password.get()))

                createNewUser.pack()



        def Register_User(self,username,password):

                global userDatabase
                
                if(not username or not password):
                        return

                Login_User = username

                Login_Password = password

                # insert details into a textfile to store

                with open("user_info.txt") as f:

                         NumberofUsers = len(f.readlines())

                if (NumberofUsers == 10):

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

                                        userDatabase[username]= User(username,password,parameters)#create add user to the dictionary instance to reference for login

                                        self.controller.show_frame(PageOne)#return to login page after registration

                                        return

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

               global PacingModesList
               
               PacingModesList = {

                        'AOO':[1,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0],

                        'AAI':[1,1,0,1,0,1,0,1,0,0,1,1,1,1,0,0,0,0],

                        'VOO':[1,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],

                        'VVI':[1,1,0,0,1,0,1,0,1,1,0,0,1,1,0,0,0,0],

                        'AOOR':[1,1,1,1,0,1,0,0,0,0,0,0,1,1,1,1,1,1],

                        'AAIR':[1,1,1,1,0,1,0,1,0,0,1,1,1,1,1,1,1,1],

                        'VOOR':[1,1,1,0,1,0,1,0,0,0,0,0,1,1,1,1,1,1],

                        'VVIR':[1,1,1,0,1,0,1,0,1,1,0,0,1,1,1,1,1,1]
                }

               #before we add the value to the string, we have to validate it based on if statements?

               #then add them all to a final string to update the parameter

               global dropVar

               dropVar =StringVar()

               global form

               form=[]

               def checkComm(self):

                       return False

               Button(self, text="Log Out", command= lambda: self.controller.show_frame(PageOne)).grid(row=0,column=1) 

        #this section would have to be inside the serial communication loop
        #        if checkComm(self) == True:

        #                Label(self,text = "Device is IS communicating with the DCM").grid(row=1, column=0,pady=20)

        #                Label(self,text ="o",fg = "green").grid(row=1, column=1,pady=20)

        #        elif checkComm(self) == False:

        #                Label(self,text = "Device is NOT communicating with the DCM").grid(row=1, column=0,pady=20)

        #                Label(self,text ="o",fg = "red").grid(row=1, column=1,pady=20)



               Button(self, text="Update Parameters", command=self.updateParameters).grid(row=2,column=1)

               Label(self, text="Parameters",font=("Calibri",15)).grid(row=2, column=0,pady=20)

               Label(self, text="p_pacingMode").grid(row=3, column=0)

               Label(self, text="PERMANENT").grid(row=3, column=1)

               

               Label(self, text="p_pacingState").grid(row=4, column=0)



               dropVar.set('   ') #default choice

               OptionMenu(self,dropVar,*PacingModesList.keys(), command=self.form).grid(row=4,column=1)

        

        def getParams(*args):

                global validParams

                validParams = {
                        'Lower Rate Limit':[str(x) for x in range(30,55,5)]+[str(x) for x in range(50,91,1)]+[str(x) for x in range(90,180,5)],
                        'Upper Rate Limit':[str(x) for x in range(50,180,5)],
                        'Maximum Sensor Rate':[str(x) for x in range(90,180,5)],
                        'Atrial Amplitude':['Off']+[str(x*0.1) for x in range(5,36,1)]+[str(x*0.1) for x in range(35,75,5)],
                        'Ventricular Amplitude':['Off']+[str(x*0.1) for x in range(5,33,1)]+[str(x*0.1) for x in range(35,75,5)],
                        'Atrial Pulse Width':['0.05']+[str(x*0.1) for x in range(1,20,1)],
                        'Ventricular Pusle Width':['0.05']+[str(x*0.1) for x in range(1,20,1)],
                        'Atrial Sensitivity':['0.25','0.5','0.75']+[str(x*0.1) for x in range(10,105,5)],
                        'Ventricular Sensitivity':['0.25','0.5','0.75']+[str(x*0.1) for x in range(10,105,5)],
                        'VRP':[str(x) for x in range(150,510,10)],
                        'ARP':[str(x) for x in range(150,510,10)],
                        'PVARP':[str(x) for x in range(150,510,10)],
                        'Hysteresis':['Off']+[str(x) for x in range(30,55,5)]+[str(x) for x in range(50,91,1)]+[str(x) for x in range(90,180,5)],
                        'Rate Smoothing':['Off','3','6','9','12','15','18','21','25'],
                        'Activity Threshold':['V-Low','Low','Med-Low','Med','Med-High','High','High'],
                        'Reaction Time':[str(x) for x in range(10,60,10)],
                        'Response Factor':[str(x) for x in range(1,17,1)],
                        'Recovery Time':[str(x) for x in range(2,17,1)]
                }

                mode = dropVar.get()

                maxarrayindex=len(userDatabase[currentUser].parameters[PacingModesList.keys().index(mode)])-1

                arrayindex=0

                for i in range(1,len(form),2):

                        if(arrayindex>maxarrayindex):
                                break
                        
                        elif(form[i].get() in validParams[form[i-1]['text']]):
                                userDatabase[currentUser].parameters[PacingModesList.keys().index(mode)][arrayindex]= form[i].get()
                                arrayindex+=1
                        else:
                                 tkMessageBox.showwarning("Error","Invalid Parameter Values")
                                 break
                                
        def form(self,*args):

                #global mode to reference
        

                global form

                mode = dropVar.get()

                rowIndex=5

                if(form):

                        for i in range(len(form)):

                                form[i].grid_remove()

                        form=[]



                counter =0

                #counter to see which value to use

                #have to sum across the whole parameters

                maxarrayindex=len(userDatabase[currentUser].parameters[PacingModesList.keys().index(mode)])-1

                arrayindex=0

                for i in range(len(parameters)):#set new parameters
                        if(arrayindex>maxarrayindex):

                                break

                        if(PacingModesList[mode][i]==1):

                                form.append(Label(self,text=parameters[i]))

                                form[counter].grid(row=rowIndex,column=0)

                                counter+=1
                              
                                form.append(Entry(self,textvariable=StringVar()))
                                form[counter].grid(row=rowIndex,column=1)

                                counter+=1

                                arrayindex+=1

                                rowIndex+=1

        def outputToFile(self,*args):
                File = open("parameters_info.txt","w")
                for i in userDatabase:
                        File.write(userDatabase[i].getOutputData()+"\n")
                File.close()

        #update function so that the update adds to the dictionary then back to the file? or from the file then reinitialized to the dictionary

        def updateParameters(self,*args):#take string based on all of the values of the parameters

        #dictionary for the mode for index of each mode based on the string

        #each value separated by commas

                
                #update userDatabase dictonary first
                self.getParams()

                mode = dropVar.get()
                
                print('userDb')
                print(userDatabase)

                for i in userDatabase:
                        if(i==currentUser): # the current user is then appended to
                                userDatabase[currentUser].outputData= i+","

                                for mode in PacingModesList:#for loop not needed as we only need to transfer information for one mode at a time!!!




                                        if(mode=='AAIR'):
                                                userDatabase[currentUser].outputData+= mode+","       
                                                counter=0

                                                for k in PacingModesList['AAIR']:

                                                        if k==1:
                                                                
                                                                userDatabase[currentUser].outputData+= userDatabase[currentUser].parameters[0][counter]+","
                                                                counter+=1

                                                        else:
                                                                userDatabase[currentUser].outputData+= "0,"
                                        
                                        elif(mode=='VVI'):
                                                userDatabase[currentUser].outputData+= mode+","
                                                counter=0

                                                for k in PacingModesList['VVI']:

                                                        if k==1:

                                                                userDatabase[currentUser].outputData+= userDatabase[currentUser].parameters[1][counter]+","
                                                                counter+=1

                                                        else:
                                                        
                                                                userDatabase[currentUser].outputData+= "0,"

                                        elif(mode=='AOOR'):
                                                userDatabase[currentUser].outputData+= mode+","
                                                counter=0

                                                for k in PacingModesList['AOOR']:

                                                        if k==1:
                                                                        
                                                                userDatabase[currentUser].outputData+= userDatabase[currentUser].parameters[2][counter]+","
                                                                counter+=1

                                                        else:
                                                                userDatabase[currentUser].outputData+= "0,"
                                                          # write all corresponding parameters to specific mode       

                                        elif(mode=='AOO'):
                                                userDatabase[currentUser].outputData+= mode+","
                                                counter=0

                                                for k in PacingModesList['AOO']:

                                                        if k==1:
                                                                        
                                                                userDatabase[currentUser].outputData+= userDatabase[currentUser].parameters[3][counter]+","
                                                                counter+=1

                                                        else:
                                                                userDatabase[currentUser].outputData+= "0,"
                                                          # write all corresponding parameters to specific mode

                                        elif(mode=='VVIR'):
                                                userDatabase[currentUser].outputData+= mode+","
                                                counter=0

                                                for k in PacingModesList['VVIR']:

                                                        if k==1:

                                                                userDatabase[currentUser].outputData+= userDatabase[currentUser].parameters[4][counter]+","
                                                                counter+=1

                                                        else:
                                                        
                                                                userDatabase[currentUser].outputData+= "0,"
                                        
                                        elif(mode=='VOO'):
                                                userDatabase[currentUser].outputData+= mode+"," 
                                                counter=0

                                                for k in PacingModesList['VOO']:

                                                        if k==1:

                                                                userDatabase[currentUser].outputData+= userDatabase[currentUser].parameters[5][counter]+","
                                                                counter+=1

                                                        else:
                                                        
                                                                userDatabase[currentUser].outputData+= "0,"


                                        elif(mode=='AAI'):
                                                userDatabase[currentUser].outputData+= mode+","       
                                                counter=0

                                                for k in PacingModesList['AAI']:

                                                        if k==1:

                                                                userDatabase[currentUser].outputData+= userDatabase[currentUser].parameters[6][counter]+","
                                                                counter+=1

                                                        else:
                                                                userDatabase[currentUser].outputData+= "0,"
                                                                  

                                        

                                        
                                        elif(mode=='VOOR'):
                                                userDatabase[currentUser].outputData+= mode+"," 
                                                counter=0

                                                for k in PacingModesList['VOOR']:

                                                        if k==1:

                                                                userDatabase[currentUser].outputData+= userDatabase[currentUser].parameters[7][counter]+","
                                                                counter+=1

                                                        else:
                                                        
                                                                userDatabase[currentUser].outputData+= "0,"

                                                 
                self.outputToFile()


app = App()

app.mainloop()

