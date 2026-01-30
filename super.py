# super() = Function used in a chlid class to call methods from a parent class (superclass).
#           Allows you to extend the functionality of the inherited methods


class Shape:
    def __init__(self,colour,is_filled):
        self.colour=colour
        self.is_filled=is_filled

    def describe(self):
        print(f"It is {self.colour} and {'filled' if self.is_filled else 'not filled'}")
class Circle(Shape):
    def __init__(self,colour,is_filled,radius):
        super().__init__(colour,is_filled) #these will be taken from super(parent) class
        self.radius=radius
    def describe(self): # there are 2 describe methods but the class will first check the local then check the super class IT IS CALLED METHOD OVERRIDING
        super().describe()# This will allow both the describe methods to print
        print(f"It is {self.colour} and radius is {3.142*self.radius*self.radius}")
class Square(Shape):
     def __init__(self,colour,is_filled,width):
        super().__init__(colour,is_filled) #these will be taken from super(parent) class
        self.width=width
class Triangle(Shape):
     def __init__(self,colour,is_filled,width,height):
        super().__init__(colour,is_filled) #these will be taken from super(parent) class
        self.width=width
        self.height=height

circle = Circle(colour="red",is_filled=True,radius=5)
print(circle.colour)
print(circle.is_filled)
print(circle.radius)


circle.describe() # there are 2 describe methods but the class will first check the local then check the super class
#THIS IS CALLED METHOD OVERRIDING