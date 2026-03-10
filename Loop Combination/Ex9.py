num = int(input("Enter the number"))

number = str(num)
evenSum = 0
oddSum = 0
for i in range(len(number)):
    digit = int(number[i])
    if digit%2 == 0:
        evenSum = evenSum + digit
    else:
        oddSum = oddSum + digit
        
print(f"Sum of even digits: {evenSum}")
print(f"Sum of odd digits: {oddSum}")

