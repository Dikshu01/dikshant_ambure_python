# Write a program to calculate the percentage of student based on marks of any 5 subjects.
m1=int(input('Enter the marks of 1st subject:'))
m2=int(input('Enter the marks of 2nd subject:'))
m3=int(input('Enter the marks of 3rd subject:'))
m4=int(input('Enter the marks of 4th subject:'))
m5=int(input('Enter the marks of 5th subject:'))

gain_marks=m1+m2+m3+m4+m5
percentage=(gain_marks/500)*100
print(f'Percentage obtained is{percentage}')