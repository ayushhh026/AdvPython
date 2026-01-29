#Python reading file (.txt , .json , .csv)

#for txt
file_path="output.txt"
try:
    with open(file_path,"r") as file: # mode = r for read
        content=file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to access that file")

#for json
import json
file_path="output.json"
try:
    with open(file_path,"r") as file: # mode = r for read
        content=json.load(file)
        print(content)
        print(content['name'])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to access that file")

#for csv
import csv

file_path="output.csv"
try:
    with open(file_path,"r") as file: # mode = r for read
        content=csv.reader(file)
        for line in content:
            print(line)
            print(line[0]) # first element in index for each row
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to access that file")