# Write a program to check if user has entered correct userid and password.
uid="Username"
passw="user@123"
user_id=input("Enter username.:")
password=input("Enter password.:")
if(user_id==uid and passw==password):
    print("You are logged in.")
else:
    print("Username or password is incorrect.")