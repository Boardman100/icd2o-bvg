dollars = input("Insert the dollar amount: $")
ogcents = int(round(float(dollars),2)*100)
cents = ogcents

num20s = cents//2000
cents = cents-num20s*2000
num10s = cents//1000
cents = cents-num10s*1000
num5s = cents//500
cents = cents-num5s*500
numtoonies = cents//200
cents = cents-numtoonies*200
numloonies = cents//100
cents = cents-numloonies*100
numquarters = cents//25
cents = cents-numquarters*25
numdimes = cents//10
cents = cents-numdimes*10
numnickels = cents//5
cents = cents-numnickels*5
numpennies = cents//1
cents = cents-numpennies

print(f"You have {ogcents} cents")
print(f"Which is equal to {num20s} twentys, {num10s} tens, {num5s} fives, {numtoonies} toonies, {numloonies} loonies, {numquarters} quarters, {numdimes} dimes, {numnickels} nickels, and {numpennies} cents.")