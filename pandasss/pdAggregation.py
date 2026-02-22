# aggregate functions = Reduces a set of values into a single summary value
#                       Used to summarize and analyze data
#                       Often used with the groupby() function
import pandas as pd

df = pd.read_csv("pokemon.csv")

#FOR WHOLE DATA

# to find mean
print(df.mean(numeric_only=True))  #  for all numeric values in a data

# to find sum
print(df.sum(numeric_only=True)) 

# to find minimumm 
print(df.min(numeric_only=True))

#to find maximum
print(df.max(numeric_only=True)) 

# to count 
print(df.count()) # no args needed


# A SINGLE COLUMN

# to find mean
print(df["Height"].mean())  #  for all numeric values in a data

# to find sum
print(df["Height"].sum()) 

# to find minimumm 
print(df["Height"].min())

#to find maximum
print(df["Height"].max()) 

# to count 
print(df["Height"].count()) # no args needed



# GROUPBY() FUNCTION
#groups by Type1 
group = df.groupby("Type1")

#gives mean ,sum ,max, and count of height for each group of type 1
print(group["Height"].mean())

print(group["Height"].sum())

print(group["Height"].max())

print(group["Height"].count())
