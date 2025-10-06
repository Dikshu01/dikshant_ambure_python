# Write a Program to input two angles from user and find third angle of the triangle.
x=int(input("Enter the degree of the first angle:"))
y=int(input("Enter the degree of the second angle:"))
z=180-(x+y)
print(f"The degree of the third angle of the triangle is {z}.")