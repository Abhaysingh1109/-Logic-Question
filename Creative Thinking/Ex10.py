year = int(input("Enter a year: "))

century = (year + 99) // 100 

if 10 <= century % 100 <= 20:
    suffix = "th"
else:
    last_digit = century % 10
    if last_digit == 1:
        suffix = "st"
    elif last_digit == 2:
        suffix = "nd"
    elif last_digit == 3:
        suffix = "rd"
    else:
        suffix = "th"

print(f"{century}{suffix} century")