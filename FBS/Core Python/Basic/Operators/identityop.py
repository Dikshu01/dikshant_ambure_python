x=10
y=10
z=20
li1=[10,20]
li2=[10,20]

# 1. is
print(x is y)
print(li1 is li2)

print(id(li1))
print(id(li2))

print(id(x))
print(id(y))
print("------------------")

# 2. is not
print(x is not y)
print(li1 is not li2)
print("------------------")