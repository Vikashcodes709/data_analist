a = 20
b = 30
z = a+b
print(f"Sum of two number {z}")

a = int(input("Enter the first number:"))
b = int(input("Enter the Second number"))
z = a+b
print(f"the sum of two number is {z}")

a = range(5)
b = range(1,10)
c = range(1,10,2)
print(a,b,c)

for i in range(1, 11):
   print(f"{i}:Hello World")

for i in range(1,10):
   print(f"{i}")

for i in range(1,10,3):
   print(f"{i}")

'''for i in range(5,51,5):
    print(i)'''

n = int(input("Enter the number that we find the table:"))
for i in range(1, 11):
    z = n*i 
    print(f"{n} * {i} = {z}")