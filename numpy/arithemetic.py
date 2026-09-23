import numpy as np

#Scalar Arithemetic

print("Scalar Arithemetic")
print("we got an 1d array: [1,2,3]")

array = np.array([1,2,3])

print(f"array + 1: {array + 1}") # [2 3 4]
print(f"array - 2: {array - 2}") # [-1 0 1]
print(f"array * 3: {array * 3}") # [3 6 9]
print(f"array / 4: {array / 4}") # [0.25 0.5 0.75]
print(f"array ** 5: {array ** 5}") # [1 32 243]

# ELement by Element Arithemtic

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print("\n")

print("We got numpy arrays = array1: [1,2,3], array2: [4,5,6]")
print("\n")

print(f"array1 + array2: {array1 + array2}") # [5 7 9]
print(f"array1 - array2: {array1 - array2}") # [-3 -3 -3]
print(f"array1 * array2: {array1 * array2}") # [ 4 10 18]
print(f"array1 / array2: {array1 / array2}") # [0.25 0.4  0.5 ]
print(f"array1 ** array2: {array1 ** array2}") # [  1  32 729]