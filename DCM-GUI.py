#GUI FOR THE DCM CONTROLLER 
# KHANG, SID, AMITESH, DEREK
# 3k04 milestone1



# usernames will be stored in a hashtable and then checked. 

ref = {} # initally empty
 
flag = True
def newUser():
    if len(ref) >= 3:
        print("Error only 10 users allowed")
        flag = False
        
    else:
        user = input("Please enter a new username") # gets the users name for the hashtable
        password = input("please enter a password")
        ref[user] = password
        x = input("Press any key to continue")


def login():
    print("test")


while flag:
    newUser()
    print(ref)



