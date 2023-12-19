'''
Prints numbers 1-100 inclusive
i = 1
while i <= 100:
    print(i)
    i += 1

Prints even numbers 1-500 inclusive
i = 1
while i <= 500:
    if i%2 == 0:
        print(i)
    i += 1

Prints odd numbers 1-500 inclusive
i = 1
while i <= 500:
    if not i%2 == 0:
        print(i)
    i += 1

Prints numbers 100-1 inclusive
i = 100
while i >= 1:
    print(i)
    i -= 1

Prints even numbers 500-1 inclusive
i = 500
while i >= 1:
    if i%2 == 0:
        print(i)
    i -= 1

Prints odd numbers 500-1 inclusive
i = 500
while i >= 1:
    if not i%2 == 0:
        print(i)
    i -= 1

Print sum of all odd numbers 1-100
i = 1
tot = 0
while i <= 100:
    if not i%2 == 0:
        tot = tot+i
    i += 1
print(tot)

Prints string in reverse order
string = input("Input your string: ")
i = 1
output = ''
while i<=len(string):
    output = output+string[len(string)-i]
    i += 1
print(output)

Calculates factorial of an integer
integer = int(input("Input your integer: "))
i = 0
output = 1
while i<integer:
    output = output*(integer-i)
    i+=1
print(output)
'''