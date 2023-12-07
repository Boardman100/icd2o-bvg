spice = 0
num_peppers = int(input())
while num_peppers>0:
    pepper = input()
    if pepper == "Poblano":
        spice = spice+1500
    if pepper == "Mirasol":
        spice = spice+6000
    if pepper == "Serrano":
        spice = spice+15500
    if pepper == "Cayenne":
        spice = spice+40000
    if pepper == "Thai":
        spice = spice+75000
    if pepper == "Habanero":
        spice = spice+125000
    num_peppers = num_peppers-1
print(spice)