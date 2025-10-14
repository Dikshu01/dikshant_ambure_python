num=int(input("Enter a number.:"))
if(num<0):
    print(f"{num} is less than zero.")
else:
    if(0<=num<=50):
        print(f"{num} is between 0 and 50.")
    else:
        if(51<=num<=100):
            print(f"{num} is between 51 and 100.")
        else:
            if(101<=num<=150):
                print(f"{num} is between 101 and 150.")
            else:
                if(151<=num<=200):
                    print(f"{num} is between 151 and 200.")
                else:
                    print(f"{num} is greater than 200.")