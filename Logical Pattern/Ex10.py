a = int(input("Enter number a: "))
r = int(input("Enter number d: "))

n = int(input("Enter the number of terms: "))

for i in range(n):
    term = a * (r**i)
    print(term)