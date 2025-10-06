# WAP to calculate selling price of book based on cost price and discount.
CP=int(input("Enter the cost price of book:"))
D=int(input("Enter the discount on book:"))
DP=(D/100)*CP
SP=CP-DP
print(f"The discounted selling price of the book is {SP}.")