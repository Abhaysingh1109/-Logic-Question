# def binaryNumber(n):
#     if n == 0:
#         return 
    
#     return (bin(n))

# n = int(input("Enter the number:"))
# res = binaryNumber(n)
# print(res)

def binaryNumber(n):
    if n == 0:
        return
    binaryNumber(n // 2)
    print(n % 2, end="")

n = int(input("Enter the number: "))
binaryNumber(n)