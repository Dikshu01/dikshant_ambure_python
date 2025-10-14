# Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)
age=int(input("Enter the person's age.:"))
gender=input("Enter person's gender(m/f).:")
if(gender=="m"):
    if(age>=21):
        print("Eligible.")
    else:
        print("Not eligible.")
elif(gender=="f"):
    if(age>=18):
        print("Eligible.")
    else:
        print("Not eligible.")