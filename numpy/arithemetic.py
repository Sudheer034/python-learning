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

print("\n")

print("Basic Math Arithemtic")

List = [1.01, 2.9, 3.5]

print(f"np.sqrt(List): {np.sqrt(List)}") # sqrt of an num
print(f"np.round(List): {np.round(List)}") # rounding to the nearest decimal
print(f"np.ceil(List): {np.ceil(List)}") # rounding with extra offset
print(f"np.floor(List): {np.floor(List)}") # rounding with low offset

print("\n")

# COMPARISON OPERATOR

print("Comparison Operators")
print("I got an array: Plick = [1,2,3]")
Plick = np.array([1,2,3])

print(f"Plick == 3 {Plick == 3}") # [False False  True]
print(f"Plick == 3 {Plick < 3}") # [True True  False]

print("")

Plick[Plick < 2] = 0

print(f"Plick[Plick < 2] = 0:  {Plick }") # [0 2 3]