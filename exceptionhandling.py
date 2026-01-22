# exception = An event that interrupts the flow of a program 
#             (ZeroDivisionError, TypeError, ValueError)
#             1.try 2.except 3.finally


try: #try some code which can cause error
    number = int(input("Enter a number : "))
    print(1/number)
except ZeroDivisionError:
    print("You cant divide by zero IDIOT!!! ")
except ValueError: # what to print if this error occurred
    print("Enter only numbers")
# for general type use
# except Exception: this is for general

finally: # this code alwyas gets executed not based on try or except
    print("Do some cleanup here")
