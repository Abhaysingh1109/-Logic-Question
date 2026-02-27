
character = input("Enter a character: ")

if ord(character) >= 48 and ord(character) <= 57:
    print("It's a digit.")
elif ord(character) >= 65 and ord(character) <= 90 or ord(character) >= 97 and ord(character) <= 122:
    print("This is the character.")
else:
    print("Not a digit nor a character.")