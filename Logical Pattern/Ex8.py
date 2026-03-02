# Check if a number is a strong number (sum of factorials of digits = number).

num = int(input("Enter a number: "))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i
    sum += factorial
    temp //= 10
    
if sum == num:
    print(num, "is a strong number.")
else:    
    print(num, "is not a strong number.")
    