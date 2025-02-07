def greet():
    """
    Simple function printing hello
    :return: 0
    """
    print("Hello!")
    return 0

greet()
x = greet()
print(x)

def greet_improved(name):
    """
    More complex greet that tajes a name as parameter
    :param name: the name of the person to greet
    :return: None
    """
    print("Hello", name)

greet_improved("John")

def custom_op(x = 0, y = 0):
    """
    Custom op: 10x + y
    :param x: the first number
    :param y: the second number
    :return: number, 10x + y
    """
    result = 10*x + y
    return result

print(custom_op(5,8))
x = custom_op(5,8) #argument by position
print(f"The result of the custom_op is: {x}")
x = custom_op(y = 9, x = 5) #argument by name
print(f"The result of custom_op is: {x}")

#only if you define x and y in the def
print(custom_op(5)) #using default values for y
print(custom_op()) #default values for both
print(custom_op(y = 9)) #default value for x

def bond_intro(name):
    print("The name is:", name)

def bond_name(first = "James", last = "Bond"):
    return f"{last}, {first} {last}"

print(bond_name("Angelo", "Scancarello"))
bond_intro(bond_name("Angelo", "Scancarello"))
bond_intro(bond_name()) #uses default values