num=int(input("Enter a three digit number to check if its a palindrome.:"))
n=num
rem1=n%10
quo1=n//10
rem2=quo1%10
quo2=quo1//10
if(quo2==rem1):
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")