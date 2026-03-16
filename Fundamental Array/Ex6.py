num = [1,2,3,4,5,6,3,0,0,0,-1,-2,-4]
posCount = 0
negCount = 0
zero = 0
for i in num:
    if i > 0:
        posCount += 1    
    elif i == 0:
        zero += 1
    else:
        negCount += 1
print(posCount)
print(negCount)
print(zero)
        


