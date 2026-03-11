def power(a,b):
    if b == 0:
        return 1
    return a * power(a,b-1)

a = int(input("Enter the base number: "))
b = int(input("Enter the power: "))
total = power(a,b)
print(f"{a} to the power of {b} is {total}")