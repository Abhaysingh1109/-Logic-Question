def oddSum(num):
    if num == 0:
        return 0
    
    return (2*num-1) + oddSum(num-1)
num = int(input("enter the number"))
print(oddSum(num))