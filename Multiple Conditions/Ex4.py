number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if number1%number2 == 0:
    print(f"{number1} is divisible by {number2}.")
else:    
    print(f"{number1} is not divisible by {number2}.")