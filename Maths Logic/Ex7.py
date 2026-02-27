# Check if an amount can be evenly divided into 2000, 500, and 100 currency notes.
notes = int(input("Enter the amount: "))

if notes%100 == 0:
    print("The amount can be evenly divided into 2000, 500, and 100 currency notes.")
else:
    print("The amount cannot be evenly divided into 2000, 500, and 100 currency notes.")