num = int(input("Enter a number: "))

if len(str(num)) == 1:
    print("The number is single digit.")
elif len(str(num)) == 2:
    print("The number is two digit.")
elif len(str(num)) >= 3:
    print("The number is multiple digit.")