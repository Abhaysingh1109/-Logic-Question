number = int(input("Enter a number: "))

for num in range(100,999):
    if number == num:
        print("The number is in the range.")
        break
else:    
    print("The number is not in the range.")