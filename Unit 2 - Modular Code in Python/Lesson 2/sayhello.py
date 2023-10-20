def greet(name):
    if isinstance(name,(str)):
        print(f"Hello {name} how has your day been?")

name = input("Input your name: ")
greet(name)