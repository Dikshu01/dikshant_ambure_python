# WAP to find area and perimeter of the following figure(Accept the length, breadth and radius from user.).
l=int(input("Enter the length of rectangle:"))
b=int(input("Enter the breadth of rectangle:"))
r=int(input("Enter the radius of the circle:"))
area_circle=(3.147*r**2)/2
area_rectangle=(l*b)
total_area=area_circle+area_rectangle
total_perimeter=2*l+b+3.147*r
print(f"Area and perimeter of the given figure is {total_area} and {total_perimeter}.")