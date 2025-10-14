# Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)
import random
captcha=random.randint(1000,9999)
uid="Username"
passw="user@123"
user_id=input("Enter username.:")
password=input("Enter password.:")
if(user_id==uid and passw==password):
    print("Username and password verified.")
    print(f"Captcha: {captcha}")
    user_captcha=int(input("Enter the captcha.:"))
    if(captcha==user_captcha):
        print("You are logged in.")
    else:
        print("Wrong captcha.")

else:
    print("Username or password is incorrect.")