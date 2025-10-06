# WAP to calculate simple interest based on principal, rate and time.
p=int(input("Enter the principal amount:"))
r=int(input("Enter the rate of interest"))
t=int(input("Enter the time in years:"))
SI=(p*r*t)/100
print(f"Simple interest on the given principal value is {SI}.")