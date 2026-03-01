        
num = int(input("Enter a number: "))
original = num
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

if rev == original:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")