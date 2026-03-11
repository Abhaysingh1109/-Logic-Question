def countNumber(n):
    if n == 0:
        return 0
    
    else:
        return 1 + countNumber(n//10)
num = int(input("Enter the number: "))

if num == 0:
    print("Number of digits: 1")
else:
    print("Number of digits:", countNumber(num))