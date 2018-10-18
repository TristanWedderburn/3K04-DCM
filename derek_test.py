import Tkinter

file = open("credentials.txt", "w")

userArray = [None] * 10 
passArray = [None] * 10
#stores up to 10 accounts

username = input("Enter username: ")
password = input("Enter password: ")

for i in range len(userArray):
    if username == userArray[i] && password == passArray[i]:
        # checks inputted credentials
        print "Access granted"
    else if username == userArray[i] && password != passArray[i]:
        # if username is correct but password incorrect
        print "Wrong password"
    else:
        userArray.append(username)
        passArray.append(password)
        #adds new user's credentials to respective arrays
        file.write(username, password)




file.close()


