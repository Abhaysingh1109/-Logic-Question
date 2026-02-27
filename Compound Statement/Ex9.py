
bill = int(input("Enter the total bill amount: "))
amount = 0

if bill <= 100:
    amount = bill * 5
elif bill > 100 and bill <= 200:
    amount = (100 * 5) + (bill-100) * 7
elif bill > 200 and bill <= 300:
    amount = (100 * 5) + (100 * 7) + (bill-200) * 10
elif bill > 300:
    amount = (100 * 5) + (100 * 7) + (100 * 10) + (bill-300) * 15   
    
print(f"The total amount to be paid is: {amount}")   