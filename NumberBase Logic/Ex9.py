
num = int(input("Enter a number: "))

num1 = 0
num2 = 1

while num > 0:
    print(num1, end=" ")
    num1, num2 = num2, num1 + num2
    num -= 1