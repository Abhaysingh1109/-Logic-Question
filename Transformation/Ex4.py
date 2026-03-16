arr = [2,3,4,5,6,7,5,8,9,2,5,0,2,1]

number = []
for i in arr:
    if i%2 == 0:
        i = 1
    else:
        i = 0
    
    number.append(i)
print(number)