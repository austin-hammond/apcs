import math

a = str(input("Name?")) #name
b = str(input("square, rectangle, or cylinder?")) #object: square, rectangle, cylinder

width = int(input("Width?"))
depth = int(input("Depth?"))

if (b == "square" or b == "rectangle"):
    length = int(input("Length?"))
    v = float(width*length*depth)
    print(a, "needs", v, "gallons in their pool.")
elif (b == "cylinder"):
    v = float(math.pi*(width/2)*(width/2)*depth)
    print(a, "needs", v, "gallons in their pool.")
