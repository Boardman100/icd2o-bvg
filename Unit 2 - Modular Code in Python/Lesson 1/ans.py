# Function to find the absolute difference between two numbers
def absolute_difference(num1, num2):
    if all(isinstance(x, (int, float)) for x in [num1, num2]):
        return abs(num1 - num2)
    
number = float(input("Enter your number: "))
number2 = float(input("Enter your percentage: "))
print(f"{absolute_difference(number,number2):.2f}")