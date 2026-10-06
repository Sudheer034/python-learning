import numpy as np

rng = np.random.default_rng()

# basics

print(rng.integers(1, 7)) # the last index is exclusive

# size, low, high keywords

print(rng.integers(low=12, high=100, size=(3,2)))


# seed

rng2 = np.random.default_rng(seed=21)
print(rng2.integers(low=12, high=100, size=(3,2)))

# uniform method

print(np.random.uniform()) # every value has equal chance of getting it

# uniform with normal methods

rng3 = np.random

rng3.seed(seed=1)

print(rng3.uniform(low=0, high=11, size = (3,3)))

# shuffling an array

array = [1,2,3,4,5]
rng4 = np.random.default_rng()

rng4.shuffle(array)
print(array)

# choice

fruits = np.array(["apple", "coconut", "pineapple", "banana"])
fruit1 = rng4.choice(fruits)
fruit2 = rng4.choice(fruits, size=(1,3))

print(fruit1, fruit2)