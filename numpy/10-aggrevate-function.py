import numpy as np

print("Aggrevate functions are sum, mean, std(standard deviation), var, min, max and lot more")

List = np.array([[1,2,3], 
                 [4,5,6]])

# print(f"np.sum(List): {np.sum(List)}")
# print(f"np.mean(List): {np.mean(List)}")
# print(f"np.std(List): {np.std(List)}")
# print(f"np.var(List): {np.var(List)}")
# print(f"np.min(List): {np.min(List)}")
# print(f"np.max(List): {np.max(List)}")
# print(f"np.argmin(List): {np.argmin(List)}")
# print(f"np.argmax(List): {np.argmax(List)}")

print(f"np.sum(List, axis=0): {np.sum(List, axis=0)}") # the high dimension, or in coordinates first, (column add)
print(f"np.sum(List, axis=1): {np.sum(List, axis=1)}") # the second highest dimension(row add)