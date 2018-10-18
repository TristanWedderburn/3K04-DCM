#GUI FOR THE DCM CONTROLLER 
# KHANG, SID, AMITESH, DEREK
# 3k04 milestone1



# usernames will be stored in a hashtable and then checked. 

ref = {} # creates an empty dictonary (also know as hashtable)
 
flag = True
def newUser():
    if len(ref) >= 3: # 3 only used so you donth have to type 10 
        print("Error only 10 users allowed")  
        x = input("press any key to continue") # temporary buffer
        
    else:
        user = input("Please enter a new username") # gets the users name for the hashtable
        password = input("please enter a password") # propmpts user for input.
        ref[user] = password # adds new key--value pair into the dictonary 
        x = input("Press any key to continue") # buffer to stop  this is temporary 


def login():
    print("test")


while flag:
    newUser() # calling newUser function
    print(ref) # prints out the new ref 



