# Decorator = A function that extends the behavior of another function
#             w/o modifying the base function
#             Pass the base function as an argument to the decorator
#      @add_sprinkles  Decorator
#      get_ice_cream("vanilla") extens the behavior of another function

def add_sprinkles(func): # takes argument as function
    def wrapper(*args,**kwargs):# it is necessary to call a nested function inside a decorator function
        print("You added sprinkles ---")
        func(*args,**kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args,**kwargs):# use *args,**kwargs when base function has arguments
        print("You add fudge---- ")
        func(*args,**kwargs)
    return wrapper

@add_sprinkles #this is a decorator
@add_fudge  # you can apply more than one decorators
def get_ice_cream(flavour):
    print(f"Here is your {flavour} ice cream 🍧")

get_ice_cream("vanilla")# the decorator gets executed whenever the main code is running

