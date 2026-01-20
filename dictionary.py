# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA":"Washington D.C.",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}
# to get all the functions of the dict
print(dir(capitals))

#TO get a value from a dict
print(capitals.get("USA"))

# looping if not in key value pair

if capitals.get("Russia"):
    print("That capital exists")
else:
    print("That capital doesnt exists")

# update the dictionary

capitals.update({"Japan":"Tokyo"})
print(capitals)

# to pop an latest value in dict 
capitals.popitem() # japan : tokyo will be poped out as it is new
print(capitals)

#capitals.clear() empty the dict


keys=capitals.keys()
print(keys) # gives keys

for key in capitals.keys():
    print(key)

values = capitals.values() 
print(values) # gives values
for value in capitals.values():
    print(value)

items=capitals.items() # gives result in dictionary of tuples  [(tuple),(tuple),(tuple)]
print(items)
for item in capitals.items():
    print(item)

for key,value in capitals.items():
    print(f"{key}:{value}")
