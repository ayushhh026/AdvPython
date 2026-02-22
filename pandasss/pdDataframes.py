# DataFrame = A Tabular data structure with rows AND columns.(2 Dimensional)
#             similar to an Excel spreadsheet
import pandas as pd
#Dictionary

data = {"Name" : ["Spongebob" , "Patrick", "Squidward"],
        "Age"  : [30,35,50]
        }

#DataFrame
df = pd.DataFrame(data,index = ["Employee1", "Employee2", "Employee3"])

print(df) # To display all
print("-------------------------")
#To select single row
print(df.loc["Employee1"])#Index number to access
print("-------------------------")

# using integer intdex
print(df.iloc[2])
print("-------------------------")

# Add new column
df["Job"] = ["Cook", "N/A", "Cashier"]
print(df)
print("-------------------------")

#Add a new row
new_row = pd.DataFrame([{"Name" : "Sandy", "Age" : 28, "Job" : "Engineer"},
                        {"Name" : "Eugene", "Age" : 60,"Job" : "Manager"}],
                        index=["Employee4","Employee5"]) # To add much rows use as much dictionaries in the list
#Concat to existing df
df = pd.concat([df,new_row])
print(df)

print(df["Job"])