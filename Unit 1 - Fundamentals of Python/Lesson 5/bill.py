drink = float(input("Enter the cost of your drink: "))
app = float(input("Enter the cost of your appetizer: "))
entree = float(input("Enter the cost of your entree: "))
dessert = float(input("Enter the cost of your dessert: "))
tip = float(input("Enter the tip rate as a percentage(eg. 15% -> 15): "))
subtotal = drink+app+entree+dessert
tip_percent = tip/100
tip_cost = subtotal*tip_percent
total_cost = tip_cost+subtotal

print("\n")
print("Bill Summary:")
print(f"Subtotal: ${subtotal}")
print(f"Tip({tip}%): ${tip_cost}")
print(f"Total Cost: ${total_cost}")