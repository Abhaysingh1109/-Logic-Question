def evenNum(n):
    if n == 0:
        return
    evenNum(n-1)
    if n%2 ==0:
        print(n)
n = int(input("Enter the number: "))
evenNum(n)