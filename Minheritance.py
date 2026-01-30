# Multiple inheritance = inherit from more than one parent class C(A,B)
#   A     B   - Parent
#    \   /
#      C      - Child

# Multilevel inheritance = inherit from a parent which inherits from another parent C(B) <- B(A) <- A
#      A
#      |
#      B(A)
#      |
#      C(B)

class Animal:
    def __init__(self,name):
        self.name = name
        



    def eat(self):
        print(f"This {self.name} is eating")
    
    def sleep(self):
        print(f"This {self.name} is sleeping")
class Prey(Animal):
    def flee (self):
        print(f"This {self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"This {self.name} is hunting")

class Hawk(Predator):
    pass

class Rabbit(Prey):
    pass

class Fish(Prey,Predator):
    pass

rabbit = Rabbit("Bugs")
hawk =Hawk("Tony")
fish = Fish("Nemo")

rabbit.eat()

#fish is multiple inheritance
fish.flee()
fish.hunt()

#multilevel inheritance
fish.eat()
fish.sleep()