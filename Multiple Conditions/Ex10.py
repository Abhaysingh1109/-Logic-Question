month = int(input("Enter the month number (1-12): "))

if month in [1, 3, 5, 7, 8, 10, 12]:
    print("The month has 31 days.")
elif month in [4, 6, 9, 11]:
    print("The month has 30 days.")
elif month == 2:
    print("The month has 28 or 29 days.")
else:
    print("Invalid month number.")