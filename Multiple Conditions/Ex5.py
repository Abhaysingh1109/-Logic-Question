greet = int(input("Enter the hour of the day (0-23): "))

if greet < 12:
    print("Good morning!")
elif greet < 18:
    print("Good afternoon!")
else:
    print("Good evening!")