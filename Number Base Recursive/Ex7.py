def numDigit(n):
    if n==0:
        return
    
    numDigit(n//10)
    print(word[n%10],end=' ')
    
word = ['zero','one','two','three','four','five','six','seven','eight','nine']

n = int(input("Enter the number:"))
numDigit(n)
print()


