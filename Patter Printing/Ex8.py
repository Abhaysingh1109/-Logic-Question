n = int(input("Enter the number of rows: "))


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j < n - i + 1:
            print("b", end="")
        else:
            if (j + i) % 2 == 0:
                print("*", end="")
            else:
                print("b", end="")
    print()
    
    
# This question is little bit complex I'll be solve later


# print

# bbbb*
# bbb*b*
# bb*b*b*
# b*b*b*b*
# *b*b*b*b*