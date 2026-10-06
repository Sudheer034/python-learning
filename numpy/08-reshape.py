import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12]) # this is an 1-D array

# we can reshape an array from 1-D array to 2-D array or high n-D array by using reshape function
# Note: the number of elements needs to be satisfy the equal number in each elements

# Syntax for reshape method: array.reshape(layer, row, column), layer can be ignored if you use two parameters, similar to function overloading in C++

print(array.shape)

array = array.reshape(2, 6) # 2 * 6 is 12, satisfies the number of elements

print(array)
print(array.shape)

# we can use -1 as parameter, numpy recognises to settle
# ex: 

array = array.reshape(-1, 1)
print(array)
print(array.shape)
