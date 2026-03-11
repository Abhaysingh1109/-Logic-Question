def oddNum(n):
    if n ==0:
        return
    oddNum(n-1)
    
    if n%2!=0:
        print(n)
n = int(input("Enter the number: "))
oddNum(n)