hour= int(input("Enter the time in hours (0-23):"))
minute= int(input("Enter the time in minutes (0-59):"))

print("The time is:",hour,":",minute)

hours = 30 * hour + 0.5 * minute
minutes = 6 * minute

angle = abs(hours - minutes)
print(angle)
smallerAngle = min(angle, 360 - angle)

print("The smaller angle between the hour and minute hands is:", smallerAngle, "degrees.")