import numpy as np

a = [1,2,3]
ar = np.array(a)

print("list vs numpy list:")
print(f"list [1,2,3] * 2: {a*2}") # [1,2,3,1,2,3]
print(f"numpy list [1,2,3] * 2: {ar*2}") # [2,4,6]

print("\n")

List = np.array([[1,2,3],[4,5,6]])

print("Indexing for Numpy for High dimensional array:")
print("ex: List = np.array([[1,2,3],[4,5,6]])")
print(f"The indexing is accessed by List[0,0]: {List[0,0]}") # 1

# List[3d-index, 2d-index, 1d-index]

print("\n")

print("Checking for which dimensional array:")
print(f"we'll use List.ndim: {List.ndim}") # ndim : n-dimensional
print(f"Shape of List.shape: {List.shape}")