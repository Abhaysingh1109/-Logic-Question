# Take a 3-digit number and check if all digits are distinct.
number1 = int(input("Enter the first number: "))

num = set(str(number1))
if len(num) == 3:
    print("All digits are distinct.")
else:    
    print("Digits are not distinct.")
