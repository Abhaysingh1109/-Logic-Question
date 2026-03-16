terms = int(input("Enter the number you want:"))
number = []
for i in range(1,terms+1):
    num = (int(input(f'Enter the number{i}:')))
    number.append(num)

print(f'The number taken by user:{number}')    
