import math
item1 = float(input("What was the celery's price: "))
item2 = float(input("What were the milk's price: "))
item3 = float(input("What was the bread's price: "))
totalcost = round(((item1+item2+item3)*1.13),2)
print(f"The total cost of the items(with tax) is: ${totalcost}")