# Series = A Pandas 1-Dimensional labeled array that can hold any data type
#          Think of it like a single column in a spreadsheet(1-Dimensional)
import pandas as pd

#USING LIST
data = [100,102,104,201,202]

series = pd.Series(data,index=["a","b","c","d","e"]) # arranges data in single column with index label
print(series)

#Access a value in a series using loc
print(series.loc["a"]) # loc = location by label

# change a value
series.loc["c"] = 200
print(series)

#Access a value in a series using iloc = integer by location
print(series.iloc[1])# uses index numbers

#Filter value to return based on condition
print(series[series>=200]) # return rows which match the conditions

#----------------------------------------------------------------------------------

calories = {"Day 1" : 1750, "Day 2" : 2100, "Day 3" : 1700}

series = pd.Series(calories)

print(series)

# update a value
series.loc["Day 3"] +=500
print(series.loc["Day 3"])

# filter by value
print(series[series >=2000])