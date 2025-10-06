# Write a program to enter P, T, R and calculate simple Interest.
p=int(input("Enter the principal amount:"))
t=int(input("Enter the duration in years:"))
r=int(input("Enter the rate of interest:"))
si=(p*t*r)/100
print(f"The simple interest for the given values is {si}.")