num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1> 0 and num2 > 0:
    sum = num1 + num2
    sum  = sum < 100
    if sum:
        print("The sum of the two numbers is less than 100.")
    else:
        print("The sum of the two numbers is greater than or equal to 100.")
else:
    print("Both numbers should be positive.")