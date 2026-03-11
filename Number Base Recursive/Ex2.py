def revNum(n,rev =0):
    if n == 0:
        return rev
    
    else:
        return revNum(n // 10, rev * 10 + n % 10)

n = 123
total = revNum(n)
print(total)
