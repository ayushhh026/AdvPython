# @property = Decorator used to define a method as a property (It can be accessed like an attribute)
#             Benefit: Add additional logic when read, write, or delete attributes
#             gives you getter(to read), setter(to write) and deleter(to delete) method

class Reactangle:
    def __init__(self,width,height):
        self._width=width  #  using _ with a variable makes it protected variable to be used in private internally
        self._height=height
    @property
    def width(self):
        return f"{self._width:.1f}cm"# there are getter methods used to read
    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter
    def width(self,new_width):
        if new_width >0:
            self._width = new_width
        else:
            print("Width must be greater than 0 ")
        
    @height.setter
    def height(self,new_height):
        if new_height >0:
            self._width = new_height
        else:
            print("Height must be greater than 0 ")

    @width.deleter
    def width(self):
        del self._width
        print("width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted")
rectangle=Reactangle(3,4)


rectangle.width = 0
rectangle.height= 9


print(rectangle.width)
print(rectangle.height)

# to delete an attribute
del rectangle.width
del rectangle.height