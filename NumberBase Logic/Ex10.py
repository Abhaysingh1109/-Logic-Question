# Print sum of first n terms of Fibonacci series.

num = int(input("Enter a number: "))

num1 = 0
num2 = 1
totalSum = 0
while num > 0:
    
    print(num1,end = " ")
    totalSum += num1
    num1,num2 = num2,num1+num2
    num-=1
print()
print(totalSum)