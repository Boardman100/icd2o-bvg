import math
b = int(input("Input b: "))
c = int(input("Input c: "))
num1 = b/2
num2 = num1**2
num3 = num2-c
num4 = math.sqrt(num3)
root1=  num1-num4
root2 = num1+num4
print(f"Roots are: {root1} and {root2}")
