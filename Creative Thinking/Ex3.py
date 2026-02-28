day = int(input("Enter a day (1-31): "))
month = int(input("Enter a month (1-12): "))

if month in [1,3,5,7,8,10,12] and 1 <= day <=31:
    print("The date is valid.")
elif month in [4,6,9,11] and 1 <= day <=30:
    print("The date is valid.")
elif month == 2 and 1 <= day <=29:
    print("The date is valid.")
else:
    print("The date is invalid.")