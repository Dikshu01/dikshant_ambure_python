# Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.
x=int(input("Enter the amount:"))
notes_2000=x//2000
ra1=x%2000
notes_500=ra1//500
ra2=ra1%500
notes_100=ra2//100
ra3=ra2%100
notes_50=ra3//50
ra4=ra3%50
notes_10=ra4//10
ra5=ra4%10
notes_5=ra5//5
ra6=ra5%5
notes_1=ra6//1
print(f"2000 Rs. Notes:{notes_2000}\n500 Rs. Notes:{notes_500}\n100 Rs. Notes:{notes_100}\n50 Rs. Notes:{notes_50}\n10 Rs. Notes:{notes_10}\n5 Rs. Coins:{notes_5}\n1 Rs. Coins:{notes_1}")