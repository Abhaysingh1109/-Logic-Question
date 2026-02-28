n = int(input("Enter a number: "))

prod = 1

temp = n

while temp > 0:
    digit = temp %10
    prod *= digit
    temp = temp //10
print(prod)
    