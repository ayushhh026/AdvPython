import pandas as pd

df = pd.read_csv("pokemon.csv", index_col="Name") # Using a custom label instead of 0 1 2 
# Now Name is a index value you can access Loc using names
# SELECTION BY COLUMN

#Single column
print(df["Height"].to_string()) # For all name 

#Multiple column
print(df[["Height", "Weight"]]) # for multiple column use List inside the df[]


# SELECTION BY ROW/S
# use loc or iloc
#using index
print(df.loc["Pikachu"])

# To get only selected columns as output
print(df.loc["Pikachu",["Height","Weight"]])

# To select a range of Rows
print(df.loc["Charizard":"Blastoise",["Height","Weight"]])
# give output from Charizard to Blastoise

# using integer index
print(df.iloc[149])

#for a range of rows
print(df.iloc[0:11:2 ,0:3]) # rows 0 to 10 with step of 2 , and columns 0 to 2


 # User enter pokemon name and we search and give all the attributes
pokemon = input("Enter the name of pokemon : ").capitalize()

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")