for num in range(1, 501):
    original = num
    reverse = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp = temp // 10

    # if original == reverse:
    #     print(num)
        
        
# using string

# for num in range(1, 501):
#     if str(num) == str(num)[::-1]:
#         print(num)