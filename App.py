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

                global userDatabase
                userDatabase = self.getRef()

                

                #all of the pssible parameters

                global parameters

                parameters=['Lower Rate Limit','Upper Rate Limit','Maximum Sensor Rate',

                 'Atrial Amplitude','Ventricular Amplitude','Atrial Pulse Width','Ventricular Pusle Width',

                 'Atrial Sensitivity','Ventricular Sensitivity','VRP','ARP','PVARP','Hysteresis',
                'Rate Smoothing','Activity Threshold','Reaction Time','Response Factor','Recovery Time']



                # string or array for data structure?



                #all of the possible mode codes

                #each mode is represented as an index in the parameters array



                #to finish the rest of the codes

                # global AOO=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]

                # global AAI=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]

                # global VOO=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]

                # global VVI=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]

                # global VDD=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]

                # global DOO=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]

                # global DDI=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]

                # global DDD=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]

                # global AOOR=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]

                # global AAIR=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]

                # global VOOR=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]

                # global VVIR=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]

                # global VDDR=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]

                # global DOOR=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]

                # global DDIR=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]

                # global DDDR=[1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]



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
                userDatabase = {}
                global outputData
                outputData = ""

                 #if no users, return empty database



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



                if(not (os.stat("user_info.txt").st_size == 0)):#not empty

                        f = open("user_info.txt","r")



                        for line in f.readlines():

                                loginInfo = line.split(" ")

                                username = loginInfo[0]

                                password = loginInfo[1].strip("\n")

                                

                                self.temp_parameters =[]

                                for i in range(len(PacingModesList.keys())):

                                        self.temp_parameters.append(

                                                (["0"]*PacingModesList[PacingModesList.keys()[i]].count(1)))



                                if(len(loginInfo)>2):

                                        for i in range(2,len(loginInfo)-1):#initialize any parameters stored for the user

                                                paramters[i-3]=loginInfo[i]



                                userDatabase[username] =User(username, password, self.temp_parameters,outputData)

                        f.close()

                return userDatabase        

                

        def Login_User(self,usernameInput,passwordInput):

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

        def __init__(self,name,password,parameters,ouputData):

                self.name = name

                self.outputData = outputData

                self.password = password

                self.parameters = parameters#each index stores the parameters of the modes as a string?



        def getName(self):

                return self.name



        def getPassword(self):

                return self.password

        

        def getParameters(self):

                return self.parameters#returns object
        
        def getOutputData(self):
                return self.outputData



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

                                        userDatabase[username]= User(username,password,parameters,outputData)#create add user to the dictionary instance to reference for login

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

               #before we add the value to the string, we have to validate it based on if statements?

               #then add them all to a final string to update the parameter

               global dropVar

               dropVar =StringVar()

               global form

               form=[]



               def checkComm(self):

                       return False



               Button(self, text="Log Out", command= lambda: self.controller.show_frame(PageOne)).grid(row=0,column=1) 

               

               if checkComm(self) == True:

                       Label(self,text = "Device is IS communicating with the DCM").grid(row=1, column=0,pady=20)

                       Label(self,text ="o",fg = "green").grid(row=1, column=1,pady=20)

               elif checkComm(self) == False:

                       Label(self,text = "Device is NOT communicating with the DCM").grid(row=1, column=0,pady=20)

                       Label(self,text ="o",fg = "red").grid(row=1, column=1,pady=20)



               Button(self, text="Update Parameters", command=self.updateParameters).grid(row=2,column=1)

               

               Label(self, text="Parameters",font=("Calibri",15)).grid(row=2, column=0,pady=20)

               Label(self, text="p_pacingMode").grid(row=3, column=0)

               Label(self, text="PERMANENT").grid(row=3, column=1)

               

               Label(self, text="p_pacingState").grid(row=4, column=0)



               dropVar.set('   ') #default choice

               OptionMenu(self,dropVar,*PacingModesList.keys(), command=self.form).grid(row=4,column=1)

        

        def getParams(*args):

                mode = dropVar.get()

                maxarrayindex=len(userDatabase[currentUser].parameters[PacingModesList.keys().index(mode)])-1

                arrayindex=0



                #instead of for loop, we want to read the label, find out which parameter, we're getting the value for, and then verify the value is within the bounds set in the documentation

                #create helper function to validate based on input label text and the value retrieved



                for i in range(1,len(form),2):

                        if(arrayindex>maxarrayindex):

                                break

                        userDatabase[currentUser].parameters[PacingModesList.keys().index(mode)][arrayindex]= form[i].get()

                        print(userDatabase[currentUser].parameters)

                        arrayindex+=1
                        

        

        # def withinBounds(self,parameter,value):

                





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
                print(userDatabase[currentUser].outputData)

                

                

                

                for i in userDatabase:
                        if(i==currentUser): # the current user is then appended to
                                userDatabase[currentUser].outputData= i+","

                                for mode in PacingModesList:#for loop not needed as we only need to transfer information for one mode at a tim
                                        
                                        if(mode=='AAT'):
                                                userDatabase[currentUser].outputData+= "0,"
                                                counter =0;

                                                for k in PacingModesList['AAT']:

                                                        if k==1:
                                                                        
                                                                userDatabase[currentUser].outputData+= userDatabase[currentUser].parameters[0][counter]+","
                                                                counter+=1

                                                        else:
                                                                userDatabase[currentUser].outputData+= "0,"
                                                        
                                                        

                                                          # write all corresponding parameters to specific mode



                                        elif(mode=='VVT'):
                                                userDatabase[currentUser].outputData+= "1,"       
                                                counter2 =0;

                                                for k in PacingModesList['VVT']:

                                                        if k==1:

                                                                userDatabase[currentUser].outputData+= userDatabase[currentUser].parameters[1][counter2]+","
                                                                counter2+=1

                                                        else:
                                                                userDatabase[currentUser].outputData+= "0,"
                                                        
                                                        

                                                         

                                        elif(mode=='VOO'):

                                                counter3 =0;
                                                userDatabase[currentUser].outputData+= "2," 

                                                for k in PacingModesList['VOO']:

                                                        if k==1:

                                                                userDatabase[currentUser].outputData+= userDatabase[currentUser].parameters[2][counter3]+","
                                                                counter3+=1

                                                        else:
                                                        
                                                                userDatabase[currentUser].outputData+= "0,"
                                                        
                print userDatabase[currentUser].outputData          
                self.outputToFile()

                                                        
     

                        
                        

        
                

                        



        #        file.writelines(["p_pacingMode"+" "+p_pacingMode+'\n',

        #                         "p_pacingState"+" "+p_pacingState+'\n'

        #                         "p_hysteresis"+" "+p_hysteresis+'\n'

        #                         "p_hysteresisInterval"+" "+p_hysteresisInterval+'\n'

        #                         "p_lowrateInterval"+" "+p_lowrateInterval+'\n'

        #                         "p_vPaceAmp"+" "+p_vPaceAmp+'\n'

        #                         "p_vPaceWidth"+" "+p_vPaceWidth+'\n'

        #                         "p_vVRP"+" "+p_vVRP+'\n'])

                

               



                win = Tk()

                win.geometry('150x150')

                win.title("Updated Paramters")

                Label(win, text="Paramters Updated",font =("Calibri",15),fg="green").grid(row=15,column=5)

               

app = App()

app.mainloop()

