def naturalNum(n):
    if n == 0:
        return 0
    return n + naturalNum(n-1)    
    
    

n = int(input("Enter the number: "))

total = naturalNum(n)

print(f"Sum of first {n} natural number is {total}")


    