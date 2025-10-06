# Write a program to swap two numbers using third variable.
x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
print(f"Before swapping x={x} and y={y}")
z=x
x=y
y=z
print(f"After swapping x={x} and y={y}")