# (a + b) > c
# (a + c) > b
# (b + c) > a 

a = int(input("Enter the first side of the triangle: "))
b = int(input("Enter the second side of the triangle: "))
c = int(input("Enter the third side of the triangle: "))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print("The sides can form a triangle.")
else:    
    print("The sides cannot form a triangle.")