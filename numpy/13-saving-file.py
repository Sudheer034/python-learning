import numpy as np

array = np.array([[1,2,3], [4,5,6]])

# saving
np.save("data", array)
print("Saved Successfully!")

# load

arrayX = np.load("data.npy")
print(arrayX)

print("Loaded successfully!")

# multiple arrays

array1 = np.array([1,2,3,4])
array2 = np.array([1.1,2.2,3.3,4.4])

np.savez("dataZ", array1, array2) # z for zip
print("Saved Zip successfully")

arrays = np.load("dataZ.npz")
print(arrays)

array3 = arrays["arr_0"]
print(array3)

# savez_compressed functions same as savez, but with less memory