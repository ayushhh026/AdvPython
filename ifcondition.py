# if = Do some code only IF some Condition is True 
# Else Do something else
# you can also use elif for mulitple if statements inside a nested if

age = int(input("Enter your age : "))

if age<0:
    print("You haven't been born yet ! ")
elif age<= 18 :
    print(f"Your age is {age} which is not legal")
else:
    print(f"Your age is {age} and you are legal")


response = input("Would you like some food (Y/N): ")
# To Check if 2 values are equal then se == operator
if response== "Y":
    print("Have some Food ")
elif response == "N":
    print("No Food for you ")
else:
    print("Invalid choice entered")

for_sale = True

if for_sale: # ASSUMES IT FOR TRUE CONDITION IF NOT GIVEN ANYTHING
    print("This item is for sale")
else:
    print("This item is NOT for sale")
