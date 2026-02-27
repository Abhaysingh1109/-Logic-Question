number = int(input("Enter a number: "))

num = str(number)
if len(num) == 3:
    if num[1]>num[0] and num[1]>num[2]:
        print(f"The middle digit {num[1]} is the greatest.")
    elif num[1]<num[0] and num[1]<num[2]:
        print(f"The middle digit {num[1]} is the smallest.")
    else:
        print(f"The middle digit {num[1]} is neither the greatest nor the smallest.")
else:
    print("Please enter a 3-digit number.")