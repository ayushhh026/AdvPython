import pandas as pd
# csv = commma separated values
# json = JavaScript Object Notation

#For csv
df = pd.read_csv("pokemon.csv")

print(df) # truncatedd data gives first 5 and last 5

#To print all data
print(df.to_string())


# For json
df = pd.read_json("usd.json")
print(df)