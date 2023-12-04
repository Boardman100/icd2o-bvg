import random
day = 1
def settinggen():
    temp = random.randint(-5, 40)
    luck = random.randint(1, 1.75)
    weather = ""
    if temp >= -5 and temp < 0:
        weather = "Hailstorm"
    if temp >= 0 and temp < 10:
        weather = "Rainy"
    if temp >= 10 and temp < 20:
        weather = "Cool"
    if temp >= 20 and temp < 25:
        weather = "Warm"
    if temp >= 25 and temp < 35:
        weather = "Hot"
    if temp >= 35 and temp < 40:
        weather = "Boiling"
    return weather,luck
def num_customers(weather,luck,cups_made):
    if weather == "Hailstorm":

    if weather == "Rainy":

    if weather == "Cool":

    if weather == "Warm":

    if weather == "Hot":

    if weather == "Boiling":
while day <= 15:
    weather,luck = settinggen()
    num_customers(weather,luck)
    
    day = day+1
