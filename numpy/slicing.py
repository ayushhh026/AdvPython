import numpy as np

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

#subscript operator 
#array[start:end:step] End is exclusive which is it will print end-1 
# array[start(row,column):end:step] for all row use : symbol
# array[row(:),column(0:3):end:step] output will be 
# print(array[:,0:3]) 
# [[ 1  2  3]   this will print all row :  from colum 0 to column 3-1 = 2
#  [ 5  6  7]   for each row
#  [ 9 10 11]
#  [13 14 15]] 
print(array[2:4,0:2])  # this prints a quadrant
# [[ 9 10]
#  [13 14]]
