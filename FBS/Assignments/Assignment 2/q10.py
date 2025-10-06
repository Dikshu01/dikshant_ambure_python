# Write a program to reverse three-digit number.
num=int(input("Enter a three digit number:"))
num2=num
d1=num2%10
num2=num2//10
d2=num2%10
d3=num2//10
print(f"{d1}{d2}{d3}")