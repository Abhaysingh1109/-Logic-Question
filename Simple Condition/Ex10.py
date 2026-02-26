
chara = input("Enter a character: ")

if ord(chara) >=97 and ord(chara) <=122:
    print("The character is a lowercase letter.")
elif ord(chara) >=65 and ord(chara) <=90:
    print("The character is an uppercase letter.")
elif ord(chara) >=48 and ord(chara) <=57:
    print("The character is a digit.")
else:
    print("The character is a special character.")