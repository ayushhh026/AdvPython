# List = [] ordered and mutable i.e can be changed . Duplicates OK

#list
fruits = ["apple","orange","banana","coconut"]

print(fruits[0])# indexing to call each element
# you can also do slicing like [start:end:step]
print(fruits[::-1])

#iterate using for loop
for fruit in fruits:
    print(fruit)

# to get diff functions of list
print(dir(fruits))
# to get description you can use help() function

#to find len
print(len(fruits))

# using IN operator you can find if an element is there in a list or collection
print("apple" in fruits)

# mutable change the list
fruits[1]="Banana"

for fruit in fruits:
    print(fruit)

# list operation


# add element on last of the list 
fruits.append("grapes")
print(fruits)

# to remove an element
fruits.remove("apple")
print(fruits)

# insert value at given index .insert(index,name)
fruits.insert(0,"pineapple")
print(fruits)

# sort in order
fruits.sort()
print(fruits)

# to reverse the order
fruits.reverse()
print(fruits)

# to clear a list 
# fruits.clear()
# print(fruits)


# find index of a valuee
print(fruits.index("banana"))

#count the frequency
print(fruits.count("banana"))