for num in range(1, 100):
    original = num
    temp = num

    while temp > 0:
        digit = temp % 10
        temp = temp // 10

    if original%3 ==0:
        print(num)
