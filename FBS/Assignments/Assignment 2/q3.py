# Convert distant given in feet and inches into meter and centimeter.
f=int(input("Enter the distance in feet:"))
i=int(input("Enter the distance in inches:"))
ni=(f*12)+i
cm=ni*2.54
m=cm//100
ncm=cm%100
print(f"The distance in feet and inches is {m} meters and {ncm} cm.")