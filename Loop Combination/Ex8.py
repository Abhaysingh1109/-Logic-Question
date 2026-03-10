n = int(input("Enter the number:"))

for i in range(1,n+1):
    fact = 1
    for j in range(1,i+1):
        fact = fact * j
    print(f"Factorial of {i} is {fact}")