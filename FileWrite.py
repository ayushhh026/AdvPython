# Python writing files (.txt, .json, .csv)

#FOR  txt
txt_data = "I like pizza"

file_path = "output.txt" # put relative or absolute path
# modes are
# w for write or overwrite, x for create a file and write does not work with files already created
# a to append
try:      
    with open(file=file_path, mode="x") as file:  #with is used to wrap code  # automatically closes the file in with
        file.write(txt_data)
        print(f"txt file {file_path} was created")
except FileExistsError:# error for mode = x if file exists
    print("File already exists! ")

employee = ["Eugene", "Squidward", "Spongebob", "Patrick"]

file_path = "output.txt" # put relative or absolute path
try:      
    with open(file=file_path, mode="a") as file:
        for emp in employee: #with is used to wrap code  # automatically closes the file in with
            file.write("\n" + emp)
        print(f"txt file {file_path} was created")
except:
    pass

import json
# FOR json
employee = {
    "name": "Spongebob",
    "age" : "30",
    "job" : "cook"
}

file_path = "output.json"

try:
     with open(file=file_path, mode="w") as file:
          json.dump(employee, file ,indent=4)
          print(f"json file at {file_path} is created")
except:
     pass

# FOR .csv files

import csv

employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

file_path = "output.csv"

try:
     with open(file=file_path, mode="w",newline="") as file:
          writer = csv.writer(file)
          for row in employees:
               writer.writerow(row)
          print(f"csv file at {file_path} is created")
except:
     pass