arr = [2,3,6,7,2,1]

# firstNum = arr[0]
# lastNum = arr[-1]

# print(firstNum)
# print(lastNum)
temp = 0
temp = arr[0]
arr[0] = arr[-1]
arr[-1] = temp            
print(arr)
    

