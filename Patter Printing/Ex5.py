n = int(input("Enter the number  "))

for i in range(n+1):
    for j in range(i*2):
        print("*", end="")
    print()