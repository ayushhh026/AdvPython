class Car:# blueprint of object
    def __init__(self,model,year,colour,for_sale): #this is a constructor method needed to create objects
            self.model=model
            self.year = year
            self.colour =colour # instance variables all have the different version
            self.for_sale = for_sale
        
    def drive(self): # method in a class
          print(f"You drive the {self.model} which is {self.colour} in colour")# no need to define variables here
    
    def stop(self):
        print(f"you stop the {self.model} which is {self.colour} in colour ")

    def describe(self):
          print(f"{self.year} {self.model} {self.colour}")