# FIltering = Keeping the rows that match a condition

import pandas as pd

df = pd.read_csv("pokemon.csv")

tall_pokemon=df[["Height"] >= 2] # Filers all the pokemons whose height less than 2
print(tall_pokemon)
print("---------------------------------------------------------------")
heavy_pokemon = df[df["Weight"]>=100]
print(heavy_pokemon)
print("---------------------------------------------------------------")
legendary_pokemon = df[df["Legendary"] == 1] # both 1 and True will work
print(legendary_pokemon)
print("---------------------------------------------------------------")
water_pokemon = df[(df["Type1"]=="Water") | 
                      (df["Type2"]=="Water")]
print(water_pokemon)
print("---------------------------------------------------------------")
ff_pokemon=df[(df["Type1"] == "Fire") &
               (df["Type2"]== "Flying")]

print(ff_pokemon)