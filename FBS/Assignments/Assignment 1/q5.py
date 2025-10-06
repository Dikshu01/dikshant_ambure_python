# Write a program to enter P, T, R and calculate Compound Interest.
p=int(input("Enter the principal amount:"))
t=int(input("Enter the duration in years:"))
r=int(input("Enter the rate of interest:"))
ci=p*(1+r)**t
print(f"The compound interest for the given values is {ci}.")