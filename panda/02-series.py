import pandas as pd

# Series in pandas is 1D array, having indices, and we have ability to modify the indices with strings and others

data = [100, 101, 102]

series = pd.Series(data)

print(series)

# aliasing the indices

series1 = pd.Series(data, index=("a", "b", "c")) # we can pass series, the indices will become the value of that partical index
print(series1)

# locating element by index(aliased)

print(series1.loc["b"])

# locating element by index(actual)

print(series1.iloc[0])

# series with dictionary

days = {"Day 1" : "Monday", "Day 2": "Tuesday", "Day 3" : "Wednesday", "Day 4": "Thursday", "Day 5": "Friday","Day 6": "Saturday", "Day 7": "Sunday" }

series = pd.Series(days)

print(series)