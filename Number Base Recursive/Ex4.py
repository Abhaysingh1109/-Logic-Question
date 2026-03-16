def productDigit(n):
    if n == 0:
        return 1
    
    return (n%10) * productDigit(n//10)

n = int(input("Enter the digits:"))
print("This product of digit is:",productDigit(n) )