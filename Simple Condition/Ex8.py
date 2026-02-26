# Take a temperature value and print whether it is hot, warm, or cold. (Hot: above 30°C, Warm: between 15°C and 30°C, Cold: below 15°C)

temp = float(input("Enter the temperature in Celsius: "))

if temp > 30:
    print("It's hot.")
elif 15 <= temp <= 30:
    print("It's warm.")
else:
    print("It's cold.")