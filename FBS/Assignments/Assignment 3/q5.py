# Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.
s1=int(input("Enter length of first side of triangle.:"))
s2=int(input("Enter length of second side of triangle.:"))
s3=int(input("Enter length of third side of triangle.:"))
if(s1==s2==s3):
    print("Triangle is an equilateral triangle.")
elif(s1==s2 or s2==s3 or s1==s3):
    print("Triangle is an isosceles triangle.")
else:
    print("Triangle is an scalene triangle.")