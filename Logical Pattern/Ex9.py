a = int(input("Enter number a: "))
d = int(input("Enter number d: "))

n = int(input("Enter the number of terms: "))

for i in range(n):
    term = a  + (i*d)
    print(term)