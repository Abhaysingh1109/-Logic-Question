

num = int(input("Enter a number: "))
sum = 0
for i in range(1,num+1):
    if num%i ==0:
        sum = sum + i
        
        print(i)
print("The sum of all divisors is:", sum)