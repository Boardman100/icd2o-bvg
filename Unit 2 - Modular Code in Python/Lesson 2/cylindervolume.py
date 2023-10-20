def cylinder_vol(rad, height):
    return 3.14159265*rad**2*height

radius = float(input("Enter your cylinder height: "))
height = float(input("Enter your cylinder radius: "))
print(f"The product is {cylinder_vol(radius,height)}")