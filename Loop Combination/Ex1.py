
for i in range(1,101):
    num = i%10
    digit = i//10
    if (num + digit)%2 ==0:
        print(i)
    
