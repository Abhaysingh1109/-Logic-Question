list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

number = int(input("Enter a single-digit number: "))
if number >= 0 and number <= 9:
    print(f"The number you entered is: {list[number]}")
else:
    print("Please enter a single-digit number.")