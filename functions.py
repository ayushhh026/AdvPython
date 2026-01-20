# function = resuable block of code
#            place () after a funtion name to invoke / call it in the program
# any parameters if declared function_name(x) must be given in (23) when calling the function

# function to wish happy birthday 3 times

def happy_birthday(name):
    print("happy birthday to you")
    print("happy birthday to you")
    print(f"happy birthday dear {name}")
    print()

happy_birthday("bro")
happy_birthday("sis")
happy_birthday("mom")

# function to display simple invoice

def invoice(username,amount,due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due : {due_date}")

invoice("Bro",34.434,"01/01")

# return statement

# return = statement to end a function
#          and send a result back to the caller

def add(x, y):
    z= x+y
    return z
def subtract(x,y):
    z=x-y
    return z
def multiply(x,y):
    z=x*y
    return z

print(add(3,4))
print(subtract(3,4))
print(multiply(3,4))



def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " "+ last

full_name = create_name("steve","jobs")
print(full_name)