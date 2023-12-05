import random
import math
def settinggen():
    temp = random.randint(-5, 40)
    luck = random.randint(0, 50)
    weather = ""
    if temp >= -5 and temp < 0:
        weather = "stormy"
    if temp >= 0 and temp < 10:
        weather = "rainy"
    if temp >= 10 and temp < 20:
        weather = "cool"
    if temp >= 20 and temp < 30:
        weather = "warm"
    if temp >= 30 and temp < 35:
        weather = "hot"
    if temp >= 35 and temp < 40:
        weather = "boiling"
    return weather,luck
def num_customers(weather,luck,ads,price,numcups):
    if weather == "stormy":
        num_customers = math.floor(numcups*(luck/100+ads*0.1)*(0.6-price*0.01))
    if weather == "rainy":
        num_customers = math.floor(numcups*(luck/100+ads*0.1)*(1.1-price*0.01))
    if weather == "cool":
        num_customers = math.floor(numcups*(luck/100+ads*0.1)*(1.5-price*0.01))
    if weather == "warm":
        num_customers = math.floor(numcups*(luck/100+ads*0.1)*(1.7-price*0.01))
    if weather == "hot":
        num_customers = math.floor(numcups*(luck/100+ads*0.1)*(2-price*0.01))
    if weather == "boiling":
        num_customers = math.floor(numcups*(luck/100+ads*0.1)*(2.5-price*0.01))
    if num_customers > numcups:
        num_customers = numcups
    return num_customers
money = 120
day = 0
print("\nYou start with 200 cents")
while day < 15:
    day = day+1
    print(f"\nDay {day}:")
    weather,luck = settinggen()
    print(f"Today the weather is {weather}")
    pricepercup = int(input("How many cents would you like to charge per cup of lemonade? "))
    numcups = int(input(f"If cups cost 3 cents each to produce. How many cups would you like to make: "))
    numads = int(input(f"If ads cost 15 cents each. How many ads would you like to post: "))
    cupssold = num_customers(weather,luck,numads,pricepercup,numcups)
    assets = cupssold*pricepercup
    expenses = numcups*3+numads*15
    netprofit = assets-expenses
    money = money+netprofit
    print(f"Cups sold: {cupssold}")
    print(f"Assets: {assets}")
    print(f"Expenses: {expenses}")
    print(f"Net Profit: {netprofit}")
    print(f"Total Money -> {money} cents")
#calculate and print profit
#cap cup price
#cap number of cups and ads based on current money