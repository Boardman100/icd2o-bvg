# Function to calculate the area of a rectangle
def area_of_rectangle(length, width):
    if isinstance(length, (int,float)) and isinstance(width, (int,float)):
        return length*width
    else:
        return "Invalid input. Please provide numeric values of length and width"
    
# Function to check if a string contains a specific substring
def contains_cubstring(string, substring):
    if isinstance(string, str) and isinstance(substring, str):
        return substring in string
    else:
        return "Invalid input. Please provide two strings"
    