dist = float(input("Enter the distance of the trip(km): "))
kmperliter = float(input("Enter the distance that your vehicle can travel on 1 liter of gas(km): "))
priceperliter = float(input("Enter the current price of fuel for 1 liter(dollars): "))
passengers = float(input("Enter the number of passengers in the car: "))
total_fuel = dist/kmperliter
total_fuelcost = total_fuel*priceperliter
fuel_perpassenger = total_fuelcost/passengers

print("\n")
print(f"The total amount of fuel needed for the trip is {total_fuel} liters.")
print(f"The total cost of fuel for the trip is ${total_fuelcost}.")
print(f"The cost of fuel per passenger is ${fuel_perpassenger}.")