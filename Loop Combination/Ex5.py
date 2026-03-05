# num = int(input("Enter the number:"))


# while num > 0:
#     digit = num%10
#     num = num//10
    
#     if (digit > num):
#         print(digit)
#     else:
#         print(num)
#         break
    
    
num = int(input("Enter the number: "))
temp = num

largest = 0
smallest = 9

while temp > 0:
    digit = temp % 10      
    
    if digit > largest:    
        largest = digit
    if digit < smallest:   
        smallest = digit
    
    temp = temp // 10 

print("Largest digit:", largest)
print("Smallest digit:", smallest)