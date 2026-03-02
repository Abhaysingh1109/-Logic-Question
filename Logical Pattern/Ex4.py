# Find HCF (GCD) of two numbers using loops.

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

hcf = 1
for i in range(1, min(a, b)+1):
    if a%i == 0 and b%i == 0:
        hcf = i
print("The HCF (GCD) of", a, "and", b, "is:", hcf)