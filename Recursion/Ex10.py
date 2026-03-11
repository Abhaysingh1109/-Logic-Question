def sumDigit(n):
    if n == 0:
        return 0
    else:
        return n% 10  + sumDigit(n//10)

n = int(input("Enter the number:"))
total = sumDigit(n)
print(f"The sum of {n} is {total}")