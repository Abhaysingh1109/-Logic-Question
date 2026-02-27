week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

day = int(input("Enter the week day number (1-7): "))

if day >= 1 and day <= 5:
    print(f"{week[day-1]} is a weekday.")
else:
    print(f"{week[day-1]} is a weekend.")