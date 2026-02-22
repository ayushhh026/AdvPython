import numpy as np

# Aggregate functions = summarize data and typically
#                       return a single value

array = np.array([[1,2,3,4,5],
                 [6,7,8,9,10]])

print(np.sum(array)) # sum of entire array
print(np.cumsum(array))# cumulative sum
print(np.mean(array)) # average
print(np.std(array)) # standard deviation spread of data
print(np.var(array)) # variance square of std
print(np.median(array))
print(np.min(array)) # minimum value
print(np.max(array)) # maximum value
print(np.argmin(array)) # position of minimum value
print(np.argmax(array)) # position of maximum value
print(np.sum(array, axis=0)) #applies addition to all the column means output will be 7 9 11 13 15
print(np.sum(array, axis=1)) #applies addition to all the row means output will be 15 40
print(np.ptp(array)) # Range = max - min