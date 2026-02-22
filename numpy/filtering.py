import numpy as np

# Filtering = Refers to the process of selecting elements
#             from an array that match a given condition

ages = np.array([[21,19,20,17,18,30,65],
                 [39,22,21,15,99,18,20]])

teenagers = ages[ages < 18]
print(teenagers) #flattens the dimensional

adults = ages[(ages >= 18) & (ages < 65)]
print(adults)

seniors = ages[ages >= 65]
print(seniors)

evens = ages[ages % 2 == 0]
print(evens)

odd = ages[ages % 2 != 0]#boolean indexing
print(odd)

#To preserve the original shape use np.where(condition,array_name,value to fill ideally 0 or -1)

adu=np.where(ages>=30,ages,0)
print(adu) # slower than boolean indexing
