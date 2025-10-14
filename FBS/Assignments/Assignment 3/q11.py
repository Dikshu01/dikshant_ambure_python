# Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.
age1=int(input("Enter the age of first person.:"))
age2=int(input("Enter the age of second person.:"))
age3=int(input("Enter the age of third person.:"))
age4=int(input("Enter the age of fourth person.:"))
age5=int(input("Enter the age of fifth person.:"))
ticket_price=100
if(age1<12):
    discount1=ticket_price-(ticket_price*0.12)
    print(f"First person is eligible for children discount.")
elif(age1>59):
    discount1=ticket_price-(ticket_price*0.5)
    print(f"First person is eligible for senior citizen discount.")
else:
    discount1=ticket_price-0
    (f"Ticket price for first person is {discount1}.")

if(age2<12):
    discount2=ticket_price-(ticket_price*0.12)
    print(f"Second person is eligible for children discount.")
elif(age2>59):
    discount2=ticket_price-(ticket_price*0.5)
    print(f"second person is eligible for senior citizen discount.")
else:
    discount2=ticket_price-0
    (f"Ticket price for second person is {discount2}.")

if(age3<12):
    discount3=ticket_price-(ticket_price*0.12)
    print(f"Third person is eligible for children discount.")
elif(age3>59):
    discount3=ticket_price-(ticket_price*0.5)
    print(f"Third person is eligible for senior citizen discount.")
else:
    discount3=ticket_price-0
    (f"Ticket price for third person is {discount3}.")

if(age4<12):
    discount4=ticket_price-(ticket_price*0.12)
    print(f"Fourth person is eligible for children discount.")
elif(age4>59):
    discount4=ticket_price-(ticket_price*0.5)
    print(f"Fourth person is eligible for senior citizen discount.")
else:
    discount4=ticket_price-0
    (f"Ticket price for fourth person is {discount4}.")

if(age5<12):
    discount5=ticket_price-(ticket_price*0.12)
    print(f"Fifth person is eligible for children discount.")
elif(age1>59):
    discount5=ticket_price-(ticket_price*0.5)
    print(f"Fifth person is eligible for senior citizen discount.")
else:
    discount5=ticket_price-0
    (f"Ticket price for fifth person is {discount5}.")

total_amount=discount1+discount2+discount3+discount4+discount5
print(f"Total amount payable is {total_amount}.")