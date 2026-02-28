number = int(input("Enter the 3-digit number: "))

first = number // 100
middle = (number // 10) % 10

last = number % 10

if first + last == middle:
    print ("The sum of the first and last digits is equal to the middle digit.")
else:
    print ("The sum of the first and last digits is not equal to the middle digit.")