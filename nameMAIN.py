# if __name__ == '__main__': (This script can be imported OR run stand alone)
#                             Functions and classes in this module can be reused
#                             without the main block of code executing

#print(__name__)  # this give output __main__



# Ex library = import library for functionality
#              when running library directly,display a help page
def main():
    print("THis is main function")
    

if __name__ == '__main__': #this tells if the code is executed in the main function or called somewhere else
                            # if called in another program then __name__ is not equal it will give the name of script instead of __main__    
    main() # this will only execute if we call the main function or else we can use other functions

# this is a Good practice to include this
#               code is modular, helps readability,leaves no global variables, avoid unintended execution