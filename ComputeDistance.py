x1 = float(input("Enter x-coordinate for point 1: "))
y1 =  float(input("Enter y-coordinate for point 1: "))

x2 = float(input("Enter x-coordinate for point 2: "))
y2 = float(input("Enter y-coordinate for point 2: "))


distance = ((x2 - x1) ** 2 + ( y2 - y1) ** 2)  ** 0.5

print("The distance between the two points is", distance)
