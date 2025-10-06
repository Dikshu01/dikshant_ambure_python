# Write a program to swap two numbers without using third variable.
x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
print(f"Before swapping x={x} and y={y}")
x=x+y
y=x-y
x=x-y
print(f"After swapping x={x} and y={y}")