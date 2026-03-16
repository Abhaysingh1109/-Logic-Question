def isPalindrome(n, rev=0, original=None):
    if original is None:
        original = n
    
    if n == 0:
        return rev == original
    
    return isPalindrome(n // 10, rev * 10 + n % 10, original)

# Test
n = 12321
if isPalindrome(n):
    print(f"{n} is a palindrome")
else:
    print(f"{n} is not a palindrome")
    
    
    
# def reverseNumber(n, rev=0):
#     """Recursively reverse a given number"""
#     if n == 0:
#         return rev
#     return reverseNumber(n // 10, rev * 10 + n % 10)

# def isPalindrome(n):
#     """Check if a number is a palindrome using recursion"""
#     original = n
    
#     # Negative numbers are not palindromes
#     if n < 0:
#         return False
    
#     # Single digit numbers are always palindromes
#     if n < 10:
#         return True
    
#     return reverseNumber(n) == original

# # Test
# n = 12321
# if isPalindrome(n):
#     print(f"{n} is a palindrome")
# else:
#     print(f"{n} is not a palindrome")
