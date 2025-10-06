# WAP to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic.
basic_salary=int(input("Enter the basic salary:"))
da=0.1*basic_salary
ta=0.12*basic_salary
hra=0.15*basic_salary
inhand_salary=basic_salary-(da+ta+hra)
print(f"The total salary of the employee is {inhand_salary}. ")