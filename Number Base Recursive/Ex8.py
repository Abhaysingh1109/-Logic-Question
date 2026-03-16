def evenSum(num):
    if num == 0:
        return 0
    
    return (2*num + evenSum(num-1))

num = int(input("enter the number"))
print(evenSum(num))