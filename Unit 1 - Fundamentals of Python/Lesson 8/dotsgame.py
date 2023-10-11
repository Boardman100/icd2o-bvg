user_name = input("Input your name: ")
title_opponent = "Opponent"
title_yourpoints = "Your Points"
title_opponentpoints = "Opponent Points"
title_boxpercent = "Box %"
print()

print("Game #1")
opponent_name1 = input("Input the name of your first opponent: ")
my_points1 = int(input("Input the number of points that you scored: "))
opponent_points1 = int(input("Input the number of points that your first opponent scored: "))
box_percentage1 = round(my_points1/36*100,2)
print()

print("Game #2")
opponent_name2 = input("Input the name of your second opponent: ")
my_points2 = int(input("Input the number of points that you scored: "))
opponent_points2 = int(input("Input the number of points that your second opponent scored: "))
box_percentage2 = round(my_points2/36*100,2)
print()

print("Game #3")
opponent_name3 = input("Input the name of your third opponent: ")
my_points3 = int(input("Input the number of points that you scored: "))
opponent_points3 = int(input("Input the number of points that your third opponent scored: "))
box_percentage3 = round(my_points3/36*100,2)
print()

print("Game #4")
opponent_name4 = input("Input the name of your fourth opponent: ")
my_points4 = int(input("Input the number of points that you scored: "))
opponent_points4 = int(input("Input the number of points that your fourth opponent scored: "))
box_percentage4 = round(my_points4/36*100,2)
print()

print("Game #5")
opponent_name5 = input("Input the name of your fifth opponent: ")
my_points5 = int(input("Input the number of points that you scored: "))
opponent_points5 = int(input("Input the number of points that your fifth opponent scored: "))
box_percentage5 = round(my_points5/36*100,2)
print()

my_points_total = my_points1+my_points2+my_points3+my_points4+my_points5
opponent_points_total = opponent_points1+opponent_points2+opponent_points3+opponent_points4+opponent_points5
box_percentage_total = round(my_points_total/180*100,2)

print(f"{title_opponent:<12}{title_yourpoints:>12}{title_opponentpoints:>19}{title_boxpercent:>9}")
print(f"====================================================")
print(f"{opponent_name1:<12}{my_points1:>12}{opponent_points1:>19}{box_percentage1:>9}")
print(f"{opponent_name2:<12}{my_points2:>12}{opponent_points2:>19}{box_percentage2:>9}")
print(f"{opponent_name3:<12}{my_points3:>12}{opponent_points3:>19}{box_percentage3:>9}")
print(f"{opponent_name4:<12}{my_points4:>12}{opponent_points4:>19}{box_percentage4:>9}")
print(f"{opponent_name5:<12}{my_points5:>12}{opponent_points5:>19}{box_percentage5:>9}")
print(f"====================================================")
print()

print("Summary:")
print(f"Total points scored: {my_points_total}")
print(f"Total points scored by opponents: {opponent_points_total}")
print(f"Percentage of points recieved: {box_percentage_total}%")