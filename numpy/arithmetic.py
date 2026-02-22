import numpy as np

# Scalar arithmetic (single value for entire array linear)
array = np.array([1.01,2.5,3.99])
# print(array ** 3) # all operation can be done like + - * / % ** power  


# Vectorized math funcs 
array = np.array([1.01,2.5,3.9])
print(np.sqrt(array))
print(np.round(array))  # you can use floor to round down and ceil to round up
print(np.ceil(array))
print(np.pi)


# Exercise
radii = np.array([1,2,3])
#Area of the circle
print(np.pi * radii **2)



# Element-wise arithmetic
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array1+array2) # adds individual element like array1[0]+array2[0] and so on
# can also perform other arithmetic + - * / etc
print(array1-array2)
print(array1*array2)
print(array1**array2)

# Comparison operators == <= >= !=
scores = np.array([91,55,100,73,82,64])

print(scores == 100) # This will return a boolean True if condition met else false 
# [False False  True False False False]

scores[scores<60] = 0
print(scores)