
# {} == dictonary 
ref = {"khang":"nguyen"} # key is the the username and value is the password
username = input()

if username in ref:
    print("Hello ", username)
else:
    print("not in ref")