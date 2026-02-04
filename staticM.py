# Static methos = A method that belongs to a class rather than any object from that class (instance)
#                 Usually used for general utility functions
# Best for utility functions that do not need access to class data

# Instance methods = Best for operations on instances of the class(objects) ex - def area(self):

class Employee:

    def __init__(self,name,position):
        self.name = name
        self.position = position
    
    def get_info(self): #instance method
        return f"{self.name} = {self.position}"
    
    @staticmethod # decorator for static method
    def is_valid_position(position): #they do not have self arguments
        valid_positions = ["manager", "cashier", "cook", "janitor"]
        return position in valid_positions
    

employee1 = Employee("Eugune","Manager")
employee2 = Employee("Squidward","Cashier")
employee3 = Employee("Spongebob","cook")

print(Employee.is_valid_position("cook")) #you can call the static method without an object but directly by class

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
