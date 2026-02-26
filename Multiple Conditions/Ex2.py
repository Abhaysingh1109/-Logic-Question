#  If the sides form a valid triangle, determine whether it is equilateral, isosceles, or scalene.

# Equilateral: a = b = c
# Isosceles: (a = b OR a = c OR b = c) and not equilateral
# Scalene: a! = b and a! = c and b! = c

a = int(input("Enter the first side of the triangle: "))
b = int(input("Enter the second side of the triangle: "))
c = int(input("Enter the third side of the triangle: "))    

if (a + b) > c and (a + c) > b and (b + c) > a:
    if a == b == c:
        print("The triangle is equilateral.")
    elif (a == b or a == c or b == c) and not (a == b == c):
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")
else:    
    print("The sides cannot form a triangle.")      
    