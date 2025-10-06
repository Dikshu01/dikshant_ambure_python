# Program to Find the Roots of a Quadratic Equation.
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
D=(b**2)-(4*a*c)
fr=(-b+D**0.5/2*a)
sr=(-b-D**0.5/2*a)
print(f"The roots of the given quadratic equation is {fr} and {sr}.")