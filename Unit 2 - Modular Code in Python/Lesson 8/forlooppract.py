'''
Prints numbers 1-100 inclusive
for number in range(1,101):
    print(number)

Prints even numbers 1-500 inclusive
for number in range(1,501):
    if number % 2 == 0:
        print(number)

Print odd numbers 1-500 inclusive
for number in range(1,501):
    if not number % 2 == 0:
        print(number)

Prints numbers 100-1
for number in range(100,0,-1):
    print(number)

Print even numbers 500-1
for number in range(500,0,-1):
    if number%2 == 0:
        print(number)

Print odd numbers 500-1
for number in range(500,0,-1):
    if not number%2 == 0:
        print(number)

Prints sum of odd numbers 1-100
i = 0
for number in range(1,101):
    if not number%2 == 0:
        i = i+number
print(i)

Reverse order of a string
string = input("Enter your string: ")
output = ''
for number in range(1,len(string)+1):
    output = output+string[len(string)-number]
print(output)

Prints factorial of a number
num = int(input("Enter your number: "))
output = 1
for i in range(1,num+1):
    output = output*i
print(output)
'''