# list comprehension =  A concise way to create lists in python
#                       Compact and easier to read than traditional loops
#             syntax    [expresion for value in iterable if condition]

#TRADITIONAL
# doubles =[]

# for i in range(1,11):
#     doubles.append(i*2)
# print(doubles)

#LIST COMPREHENSION
doubles=[i*2 for i in range(1,11)]
triples=[j*3 for j in range(1,11)]
print(doubles)
print(triples)

fruits = ["apple","orange","banana","coconut"]
fruits=[fruit.capitalize() for fruit in fruits]
fruits_char=[fruit[0] for fruit in fruits]
print(fruits)
print(fruits_char)

no=[1,-3,4,-5,3,-1,3,-4]

positive_no=[n for n in no if n>=0]
print(positive_no)
even=[n for n in no if n%2==0]
print(even)