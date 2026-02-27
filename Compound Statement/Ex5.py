# (age > 18 and income > 5 L)

age = int(input("Enter your age: "))    
income = float(input("Enter your income in lakhs: "))

if age >= 18 and income > 400000:
    print("You are eligible for the loan.")
else:
    print("You are not eligible for the loan.")