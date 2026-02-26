alphabet = input("Enter a letter: ")

if ord(alphabet) >= 97 and ord(alphabet) <= 109:
    print("The alphabet is lies between a and m.")
elif ord(alphabet) >= 110 and ord(alphabet) <= 122:
    print("The alphabet is lies between n and z.")
else:
    print("Not a valid alphabet.")