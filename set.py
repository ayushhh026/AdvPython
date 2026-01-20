# Set  = {} unordered and immutable can not be changed. No duplicates



fruits = {"apple","orange","banana","coconut","coconut"}# no duplicates coconut will be considered only once
print(fruits)

# to get all the methods that can be performed on a set
# print(dir(fruits))

# add element in a set
fruits.add("pineapple")
print(fruits)
#remove an element in a set
fruits.remove("apple")
print(fruits)

# pop first element 
fruits.pop()

# clear the set
fruits.clear()
print(fruits)

