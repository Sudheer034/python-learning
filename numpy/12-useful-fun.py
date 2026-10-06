import numpy as np

# zeros()

array = np.zeros(5) # it returns, 1-D array of zeros, this takes tuple as input

print(array)
print(array.dtype)

# ones()

array1 = np.ones((3, 1,2))
print(array1)
print(array1.dtype)

# full()

array2 = np.full((3, 1,2), 9, dtype=np.uint8) # its FULL not FILL
print(array2)
print(array2.dtype)

# eye()

array3 = np.eye(3, 2) # eye for Identity matrix, im suprised that it can do for non - nXn matrix
print(array3)
print(array3.dtype)

# empty()

array4 = np.empty((2,3))
print(array4)
print(array4.dtype)

# arange()

array5 = np.arange(1, 11, 1) # args: start: stop: step, YOU CAN EVEN USE DECIMAL NUMBERS 0.1 for step
print(array5)
print(array5.dtype)

array6 = np.linspace(0, 12, 4) # args: start: stop: num
print(array6)
print(array6.dtype)