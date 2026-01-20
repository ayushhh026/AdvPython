# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone,cup,book
#          You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

# class in other file
from carC import Car

# to constuct car object
car1 = Car("Mustang",2024,"red",False) # to invoke the constructor self is predefined

car2 = Car("BMW",2025,"orange",True)

print(car2.model)
print(car2.year)
print(car2.colour)
print(car2.for_sale)

car1.drive()
car2.stop()
car1.describe()