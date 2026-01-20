# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable separate files


# print(help("modules")) # gives all available modules
# print(help("fastapi")) # gives all available mthods in fastapi module

# import math 
# print(math.pi)

# import math as m  using ALIAS name 
# print(m.pi)


# import only specific method
# from math import pi
# print(pi)


pi = 3.14159

def square(x):
    return x**2

def cube(x):
    return x**3

# you can import these functions in another code with
# import modules
# this will allow you to use this functions directly