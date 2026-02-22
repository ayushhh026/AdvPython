import numpy as np

#Integer numbers
rng = np.random.default_rng(seed=1)# to produce same number result use seed=number 
print(rng.integers(low=1,high=101,size=3)) # numbers stored in 1D array

# for 2 d array change the size to rows and columns
print(rng.integers(low=1,high=101,size=(3,2)))

#Floating point number
# np.random.seed(seed=2) # to produce same seed
print(np.random.uniform(low=-1,high=1,size=(3,3))) # Random floating point number between a range low and high and size

array = np.array([1,2,3,4,5])
print(array)
rng.shuffle(array)
print(array)

fruits = np.array(["Apple", "orange", "banana", "pineapple"])
print(fruits)
fruits = rng.choice(fruits,size = (3,3))
print(fruits)