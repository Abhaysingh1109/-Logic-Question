date1 = int(input("Enter the first date (1-31): "))
month1 = int(input("Enter the first month (1-12): "))
date2 = int(input("Enter the second date (1-31): "))
month2 = int(input("Enter the second month (1-12): "))

if 1 <= month1 <= 12 and 1<= date1 <=31 and 1 <= month2 <= 12 and 1 <= date2 <= 31:
    if month1 < month2 or (month1 == month2 and date1 < date2):
        print("The first date come first.")
    elif month1 > month2 or (month1 == month2 and date1 < date2):
        print("The second date come first.")
    else:
        print("Both dates are the same.")
else:
    print("Invalid date or month entered.")
