number = int(input("Enter the 3-digit number: "))

fist = number // 100
middle = (number // 10) % 10
last = number % 10

add = sum([fist, middle, last])
mul= fist * middle * last

if add > mul:
    print("The sum of the digits is greater than the product of the digits.")
else:
    print("The sum of the digits is not greater than the product of the digits.")