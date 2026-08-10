a = float(input("Enter the first no. of AP: "))
d = float(input("Enter the common difference no of AP: "))
n = int(input("Enter the number of terms of AP: "))

for i in range(n):
    term = a+i*d
    print(f"the 5 terms of the AP are: {term}")
