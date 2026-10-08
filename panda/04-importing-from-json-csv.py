import pandas as pd

pokemonCSV = pd.read_csv("panda/pokemon.csv") # to read csv file :)

pokemoJSON = pd.read_json("panda/pokemon.json") # yay we loaded json too

# print(pokemonCSV.to_string()) 
# normally we get trunketted version of it, we can make it as string and print all the data

print(pokemoJSON.to_string())