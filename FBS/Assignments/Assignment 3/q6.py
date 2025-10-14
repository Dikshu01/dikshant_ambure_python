# Write a program to calculate profit or loss.
selling_price=int(input("Enter the selling price of the product.:"))
cost_price=int(input("Enter the cost price of the product.:"))
if(selling_price>cost_price):
    profit=selling_price-cost_price
    print(f"Seller made a profit of  Rs.{profit}.")
elif(cost_price>selling_price):
    loss=cost_price-selling_price
    print(f"Seller incurred loss of Rs.{loss}.")
else:
    print("Seller made neither profit nor loss.")