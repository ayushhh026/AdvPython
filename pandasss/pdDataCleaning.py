# Data Cleaning = The process of fixing,removing:
#                 incomplete, incorrect, or irrelevant data.
#                 ~80% of work done with pandas is data cleaning
import pandas as pd

df = pd.read_csv("pokemon.csv")

#1. Drop irrelevant columns
df= df.drop(columns=["Legendary", "No"])

#2. Handle missing data
# df= df.dropna(subset=["Type2"]) # drop rows missing any values
df = df.fillna({"Type2" : "None"}) # Replace not available value in Type2 with None 

#3. Fix inconsistent values
df["Type1"] = df["Type1"].replace({"Grass" : "GRASS"})  # Replace all instance of Grass in Type1 with GRASS

df[["Type1","Type2"]] = df[["Type1","Type2"]].replace({"Grass" : "GRASS",
                                                       "Fire" : "FIRE",
                                                       "Water" : "WATER"}) # for both type1 and type2

#4. Standardize text
df["Name"] = df["Name"].str.lower()

#5. Fix Data Type
df["Legendary"] = df["Legendary"].astype(bool)

#6. Remove Dupliccate Values
df = df.drop_duplicates()

print(df.to_string())