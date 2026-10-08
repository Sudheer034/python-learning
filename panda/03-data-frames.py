import pandas as pd

data = {"Pokemon": 
        ["Bulbasaur", "Ivysaur", "Venosaur", "Charmender", "Charmelean", "Charizard", "Squirtle", "Warturtle", "Blastoise"],
        "Type 1": ["Grass", "Grass", "Grass", "Fire", "Fire", "Fire", "Water", "Water", "Water"],
        "Type 2": ["None", "None", "Posionous", "None", "None", "Flying", "None","None","None"]}

# Creating a dataframe
df = pd.DataFrame(data, index=[1,2,3,4,5,6,7,8,9])

# adding a new column
df["Recorded?"] = ["Yes", "No", "No", "No", "No", "No", "No", "No", "No"]

# adding a new row
new_rows = pd.DataFrame([{"Pokemon": "Caterpie", "Type 1": "Bug", "Type 2": "None", "Recorded?":"Yes"}, {"Pokemon": "Metapod", "Type 1": "Bug", "Type 2": "None", "Recorded?":"Yes"}], index=[10,11])

df = pd.concat([df, new_rows]) # it takes an list, thats surprising

print(df)