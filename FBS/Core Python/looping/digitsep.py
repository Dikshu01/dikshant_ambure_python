num=int(input("Enter a number to seperate it's digits:"))
n=num
while(n!=0):
    rem=num%10
    num=num//10 
    print(rem)
   