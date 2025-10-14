# Input 5 subject marks from user and display grade(eg.First class,Second class ..)
marks1=int(input("Enter the marks of first subject.:"))
marks2=int(input("Enter the marks of second subject.:"))
marks3=int(input("Enter the marks of third subject.:"))
marks4=int(input("Enter the marks of fourth subject.:"))
marks5=int(input("Enter the marks of fifth subject.:"))
marks_obtained=marks1+marks2+marks3+marks4+marks5
perc=(marks_obtained/500)*100
if(41<=perc<=50):
    print("Grade obtained is 'P'.")
elif(51<=perc<=60):
    print("Grade obtained is 'E'.")
elif(61<=perc<=70):
    print("Grade obtained is 'D'.")
elif(71<=perc<=80):
    print("Grade obtained is 'C'.")
elif(81<=perc<=90):
    print("Grade obtained is 'B'.")
elif(91<=perc<=100):
    print("Grade obtained is 'A'.")
else:
    print("You failed.")