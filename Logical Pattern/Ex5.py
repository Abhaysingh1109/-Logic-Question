# find the lcm of two numbers using loops.
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

lcm = max(a, b)
print(lcm)

while True:
    if lcm%a == 0 and lcm%b == 0:
        break
    lcm += 1
print("The LCM of", a, "and", b, "is:", lcm)
    
