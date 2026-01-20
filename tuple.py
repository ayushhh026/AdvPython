# Tuple= () ordered and immutable i.e can not be changed. Duplicated OK . FASTER compared to list as they are

fruits = ("apple","orange","banana","coconut","coconut")
print(fruits)

# to get to know of all functions use dir
print(dir(fruits))

# len of tuple
print(len(fruits))

# you can use IN operator
# same as others

# index to find index no
print(fruits.index("apple"))

# to get count of word
print(fruits.count("coconut"))

#iterate over a loop
for fruit in fruits:
    print(fruit)