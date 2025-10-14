# Write a program to input all sides of a triangle and check whether triangle is valid or not.
s1=int(input("Enter length of first side of triangle.:"))
s2=int(input("Enter length of second side of triangle.:"))
s3=int(input("Enter length of third side of triangle.:"))
if(s1+s2>s3):
    print("Triangle is valid.")
elif(s2+s3>s1):
    print("Triangle is valid.")
elif(s1+s3>s2):
    print("Triangle is valid.")
else:
    print("Triangle is not valid.")