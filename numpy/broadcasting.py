import numpy as np

#BroadCasting in numpy is product of arrays having different shapes

# But if one of them has either same number or 1, they can be broadcasted

array1 = np.array([[1,2,3], 
                   [4,5,6]])

array2 = np.array([[1, 2, 3]])

print("array1 : [[1,2,3], [4,5,6]]")
print("array2 : [[1, 2, 3]]")

print("\n")

print(f"array1.shape: {array1.shape}")
print(f"array2.shape: {array2.shape}")

# Broadcasting of array1 and array2 is possible because columns are 2 and 1 if 1 is there it is accepted and for rows they both have same number of rows so it can be possible

print("BroadCasting of array1 and array2: array1 * array2")
print(array1 * array2)

# BroadCasting is like multiplication of matrices, but with restricted cases, 1x4 and 4x1 accepted. 2x3 and 3x2 isn't accepted, 4x4 and 4x1 is accepted and 2x2 and 2x2 is accepted