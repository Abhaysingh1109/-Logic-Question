def downNUmber(n):
    if n == 0:
        return
    print(n)
    downNUmber(n-1)
    
    
n = int(input("Enter the number: "))
downNUmber(n)