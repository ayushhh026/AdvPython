# membership operators = used to test whether a value or variable is found in a sequence
#                        (string,list,tuple,set,dictionary)
#                        1.in
#                        2.not in  
# returns value of true or false

word ="APPLE"

letter = input("Guess the letter in a word: ")

if  letter in word: # returns either true or false
    print(f"There is a {letter}")
else:
    print(f"The letter {letter} is not present")

email = "Py4u@gmail.com"

if "@" in email and "." in email:
    print("valid email")
else:
    print("Invalid email")