
num = int(input("Enter the number"))

for i in range(1,num+1):
    binary = bin(i)
    
    count = binary.count('1')
    
    if count%2 ==0:
        print(i)
    