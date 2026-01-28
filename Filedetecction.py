# file detection in python

import os

file_path = "C:/Users/ayush/OneDrive/Desktop/PYTHON BROCODE/test.txt"

if os.path.exists(file_path): #RETURNS TRUE OR FALSE
    print(f"The location '{file_path}' exists")
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory ")
else:
    print("Location of file doesnt exist")