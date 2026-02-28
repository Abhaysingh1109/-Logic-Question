num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

maximum = max(num1, num2, num3)  

# using the pythagonorean theorem.

if maximum == num1:
    if num1**2 == num2**2 + num3**2:
        print(f"{num1} is the greatest number and it satisfies the Pythagorean theorem.")
    else:
        print(f"{num1} is the greatest number but it does not satisfy the Pythagorean theorem.")
elif maximum == num2:
    if num2**2 == num1**2 + num3**2:
        print(f"{num2} is the greatest number and it satisfies the Pythagorean theorem.")
    else:
        print(f"{num2} is the greatest number but it does not satisfy the Pythagorean theorem.")
else:
    if num3**2 == num1**2 + num2**2:
        print(f"{num3} is the greatest number and it satisfies the Pythagorean theorem.")
    else:
        print(f"{num3} is the greatest number but it does not satisfy the Pythagorean theorem.")    
