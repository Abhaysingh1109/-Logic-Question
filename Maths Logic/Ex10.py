#Check whether a number is a perfect square (without using the square root function)
number = int(input("Enter a number: "))

for num in range(1,number+1):
    if num*num == number:
        print("The number is a perfect square.")
        break
else:    
    print("The number is not a perfect square.")