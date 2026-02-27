print("Number must be in +ve quadrant or -ve quadrant or both.\n")

axisX = int(input("Enter the x-coordinate: "))
axisY = int(input("Enter the y-coordinate: "))


if axisX > 0 and axisY > 0:
    print("The point is in the first quadrant.")
elif axisX < 0 and axisY > 0:
    print("The point is in the second quadrant.")
elif axisX < 0 and axisY < 0:
    print("The point is in the third quadrant.")
elif axisX > 0 and axisY < 0:
    print("The point is in the fourth quadrant.")
elif axisX == 0 and axisY != 0:
    print("The point is on the y-axis.")
elif axisX != 0 and axisY == 0:
    print("The point is on the x-axis.")
else:
    print("The point is at the origin.")