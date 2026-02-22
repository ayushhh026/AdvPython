import numpy as np

# Broad casting allows NumPy to perform operations on arrays 
# with different shapes by virtually expanding dimesnions
# so they match the larger arreay's shape.

# The dimensions have the same size.
# OR
# One of the dimensions has a size of 1.

array1 = np.array([[1,2,3,4]])
array2 = np.array([[1],[2],[3],[4]])

print(array1.shape)
print(array2.shape)

print(array1 * array2)

#Exercise create multiplication table

array=np.array([[1,2,3,4,5,6,7,8,9,10]])
arrayn1=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
arrayn2 = np.array([[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]])
print(array.shape)
print(arrayn1.shape)
print(array * arrayn1)

# reshape to match the shape of 2 arrays use reshape
# array.reshape(row,column) You can use -1 to let NumPy auto-calculate one dimension
# only one -1 is allowed 
# to reshape arrayn2 which has 20 numbers use reshape to match it as array
arrayn2=arrayn2.reshape(-1,10)
print(arrayn2.shape)
print(arrayn2)
print(arrayn2+array)

array1 = np.array([[1,2,3,4]])
array2 = np.array([[1,2,3,4,5,6,7,8]])

array2=array2.reshape(-1,4)

print(array1+array2)