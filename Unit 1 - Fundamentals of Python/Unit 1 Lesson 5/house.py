length = float(input("Enter the length of one wall of the house(in meters): "))
width = float(input("Enter the width of one wall of the house(in meters): "))
height = float(input("Enter the height of the house(in meters): "))
brick_cost = float(input("Enter the cost of a brick(in dollars): $"))
brick_length = float(input("Enter the length of a standard brick(in meters): "))
brick_width = float(input("Enter the width of a standard brick(in meters): "))
brick_height = float(input("Enter the height of a standard brick(in meters): "))
sa_walls = length*height*4
sa_brick = brick_length*brick_height
num_bricks = sa_walls/sa_brick
bricks_cost = num_bricks*brick_cost

print(f"The walls have an SA of {sa_walls} m^2")
print(f"The house will require {num_bricks} bricks")
print(f"The bricks will cost ${bricks_cost} in total.")