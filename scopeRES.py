# variable scope = where a variable is visib;e and accessible

# scope resolution = the order in which the variable matters (LEGB) LOCAL -> ENCLOSED -> GLOBAL -> BUILT-IN
#                     if there are e=1 in local,e=3 in enclosed,e=4 in global and e=2.71 in built in
#                     THE PROGRAM WILL PRINT THE e=1 WHICH IS A local variable
#local var

def funclocal():
    a=1 # local variable can be used only here not somewhere else
    print(a)
funclocal()

#enclosed var
def func1():
    x=1 # enclosed variable 
    def func2():
        x=2  # we use the local one as it is mere neiche
        print(x)
    func2()
func1()

# global var

y=1 # global variable declared
def funGlobal():
    print(y)
def func():
    print(y)

funGlobal()
func()


# built-in var

from math import e

def funcE():
    print(e) #built in variable

funcE()