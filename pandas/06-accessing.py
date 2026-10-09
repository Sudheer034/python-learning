import pandas as pd

df = pd.read_csv("pandas/pokemon.csv")

df.index=df["Name"] # taking names as indices :)

# BY COLUMNS

# print(df["Name"]) # accessing single column
# print(df[["Name", "Type 1"]]) # accessing multiple columns, it is bit annoying to use multiple lists, first bracket is access or create and second bracket is for put # of strings or data

# print(df["Type 1"])

# BY ROWS
# print(df.loc["Bulbasaur"]) # accessing a row.
# print(df.loc["Bulbasaur":"Blastoise"]) # accessing multiple rows, you can use similar to loops thing