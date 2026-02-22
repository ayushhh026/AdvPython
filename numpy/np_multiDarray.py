import numpy as np

# 0 dimensional array 
# array = np.array('A')

# 1 dimensional array
#array = np.array(['A','B','C'])

# 2 dimensional array 
# array = np.array([['A','B','C'], 
#                   ['D','E','F'], 
#                   ['G','H','I']])

# 3 Dimensional array
array = np.array([[['A','B','C'], ['D','E','F'], ['G','H','I']],
                  [['J','K','L'], ['M','N','O'], ['P','Q','R']],
                  [['S','T','U'], ['V','W','X'], ['Y','Z','A']]])



print(array.ndim) # shows dimensional

print(array.shape) # shows (depth,row,column)

print(array[0,0,0]) # (depth,row,column) multidimensional indexing prints firste letter of first list in first row in first column
#faster than chain indexing


#exercise
word = array[0,0,0] + array[2,0,0] + array[0,2,1]
print(word)