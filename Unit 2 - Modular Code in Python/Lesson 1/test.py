def area_of_rectangle(length, width):
    if isinstance(length, (int,float)) and isinstance(width, (int,float)):
        return length*width
    else:
        return "Invalid input. Please provide numeric values of length and width"
    
def contains_cubstring(string, substring):
    if isinstance(string, str) and isinstance(substring, str):
        return substring in string
    else:
        return "Invalid input. Please provide two strings"

def average_of_three_floats(num1, num2, num3):
    if all(isinstance(x,float) for x in [num1, num2, num3]):
        return(num1+num2+num3)/3.0
    else:
        return "Invalid input. Please provide three floating-point numbers"

def concatenate_strings(str1, str2):
    if isinstance(str1, str) and isinstance(str2, str):
        return str1+str2
    
def volume_of_cube(side_length):
    if isinstance(side_length, (int, float)):
        return side_length**3
    
