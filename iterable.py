# iterables =  An object/collection that can return its elements one at a time,
#              allowing it to be iiterated over in a loop
#list
numbers = [1,2,3,4,5]
for number in numbers:
    print(number)

# to reverse it
for number in reversed(numbers):
    print(number, end= " - ")
    
#tupple

no = (1,2,3,4,5)
for number in numbers:
    print(number)

#string
name ="Spongebob Squarepants"

for c in name:
    print(c,end=" ")
print()


#set

fruits={"apple","orange","banana","coconut"}

for fruit in fruits:
    print(fruit)


# dictionary

my_dict={"A":1,"B":2,"C":3}

for key,value in my_dict.items():
    print(key,value)