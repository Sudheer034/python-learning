import numpy as np

List = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']], 
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]])

print(f"The dimension: {List.ndim}")

print("Slicing: L[start:end:step]") #it could for more high dimensional array, L[s:e:t, s:e:t]

print("Creating a 4x4 grid: [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]]")

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12], 
                  [13,14,15,16]])

print("Lets start slice!")
print("array[1:4:2]:")
print(array[1:4:2]) # [[5 6 7 8]    <-- the starting index 
                    #   13 14 15 16] <-- the shift of 2 indices

print("\n")

print("array[::, 0]")
print(array[::, 0]) # taking all rows, but first index so column of every array
                    # [1 5 9 13]

print("\n")

print("array[0:4:2, 0: 4: 2]")
print(array[0:4:2, 0: 4: 2])  # [[1 3]
                              #  [9 11]]