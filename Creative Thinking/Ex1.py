axisX = int(input("Enter the length of the first axis: "))
axisY = int(input("Enter the length of the second axis: "))

if axisX == 0 and axisY == 0:
    print("The coordinates at the origin.")
elif axisX !=0  and  axisY == 0:
    print("The coordinates are on the X-axis.")
elif axisX == 0 and axisY != 0:
    print("The coordinates are on the Y-axis.") 
elif axisX != 0 and axisY != 0:
    print("The coordinates are in the quadrant.")