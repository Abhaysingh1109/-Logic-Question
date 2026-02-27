hour = int(input("Enter the hour (0-23): "))
minute = int(input("Enter the minute (0-59): "))

if (hour >= 0 and hour < 12) or (hour == 12 and minute == 0):
    print("It's morning.")
elif (hour >= 12 and hour < 18) or (hour == 18 and minute == 0):
    print("It's afternoon.")
elif (hour >= 18 and hour < 21) or (hour == 21 and minute == 0):
    print("It's evening.")
else:
    print("It's night.")