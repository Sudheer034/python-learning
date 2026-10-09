import pandas as pd

pokemon = pd.read_csv("panda/pokemon.csv")

print(pokemon[pokemon["Type 1"] == "Water"]) # we can filter using access operator :)

