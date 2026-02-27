number = int(input("Enter a number: "))

num = str(number)

if len(num) == 4:
    if num[0] == num[3]:
        print("The first and last digits are the same.")
    else:
        print("The first and last digits are different.")
else:
    print("Please enter a 3-digit number.")

num = int(num)