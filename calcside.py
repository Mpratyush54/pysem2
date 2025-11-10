sideA = float(input("Enter the length of side A: "))
sideB = float(input("Enter the length of side B: "))
sideC = float(input("Enter the length of side C: "))


# check for validity of triangle
if (sideA + sideB > sideC) or (sideA + sideC > sideB) or (sideB + sideC > sideA):
    s = (sideA + sideB + sideC) / 2
    area = (s * (s - sideA) * (s - sideB) * (s - sideC)) ** 0.5
    print(f"The area of the triangle is: {area}")
