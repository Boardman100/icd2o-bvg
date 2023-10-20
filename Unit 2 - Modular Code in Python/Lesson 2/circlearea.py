def circarea(radius):
    import math
    area = radius**2*math.pi
    print(f"{area}")

radius = float(input("Input your radius: "))
circarea(radius)