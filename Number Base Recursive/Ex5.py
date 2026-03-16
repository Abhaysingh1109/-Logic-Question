def GCD(a,b):
    if b == 0:
        return a
    
    return GCD(b,a%b)

a = int(input("Enter the number a:"))
b = int(input("Enter the number b:"))

result = GCD(a,b)

print(result)
