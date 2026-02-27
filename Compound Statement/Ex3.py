num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

median = num1 + num2+ num3 -max(num1, num2, num3) - min(num1, num2, num3)

print(f"The median of {num1}, {num2}, and {num3} is: {median}")