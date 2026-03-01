num = int(input("Enter a number: "))

for i in range(2,num):
    if num % i == 0:
        print(num, "is not a prime number.")
        break
    elif num == 0:
        print(num,"is whole number")
        break
else:
    print(num, "is a prime number.")
    