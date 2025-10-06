# Write a program to convert days into years, weeks and days.
d=int(input("Enter the no. of days:"))
y=d//365
rem1=d%365
w=rem1//7
rem2=rem1%7
print(f"The conversion of given days is {y} years, {w} weeks and {rem2} days.")