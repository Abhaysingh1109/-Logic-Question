number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if number1%2 == 0 and number2%2 == 0:
    print("Both numbers are even.")
elif number1%2 != 0 and number2%2 != 0:
    print("Both numbers are odd.")
else:
    print("One number is even and the other is odd.")