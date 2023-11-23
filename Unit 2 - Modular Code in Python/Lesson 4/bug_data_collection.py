def input_bug_counts(bug_type):
    return int(input(f"How many {bug_type} are there?: "))

def calculate_percent(total,count):
    return count/total*100

def input_bug_type_and_count():
    bug_type = input(f"Input bug type: ")
    count = input_bug_counts(bug_type)
    return bug_type,count

def display_table(bug1,count1,bug2,count2,bug3,count3):
    total = count1+count2+count3
    percent1 = round(count1/total*100,2)
    percent2 = round(count2/total*100,2)
    percent3 = round(count3/total*100,2)
    print("\n")
    print(f"{'Bug Type':<10}{'Count':<10}{'Percentage':<10}")
    print("-"*30)
    print(f"{bug1:<10}{count1:<10}{percent1}{'%':<10}")
    print(f"{bug2:<10}{count2:<10}{percent2}{'%':<10}")
    print(f"{bug3:<10}{count3:<10}{percent3}{'%':<10}")
    print("-"*30)
    print(f"{'Total':<10}{total:<10}{'100.00'}{'%':<10}")
bug1, count1 = input_bug_type_and_count()
bug2, count2 = input_bug_type_and_count()
bug3, count3 = input_bug_type_and_count()
display_table(bug1, count1, bug2, count2, bug3, count3)