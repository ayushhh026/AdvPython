# Contains exercise on the topic of variable TypeCasting and Input functions

# Exercise 1 Recatange Area Calc
# Area = length x width

length = float(input("Enter the length :"))  #Tip use alt + shift and down arrow key to get same line down and change the name
width = float(input("Enter the width : "))
Area = length * width

print(f"Area of reactangle with Length : {length} and Width : {width} is {Area}cm²")# To get square >> numlock on then alt+0178 


#Exercise 2 Shopping Cart Program

item = input("What Item would you like to buy : ")
price = float(input("What is the price of the item : "))
quantity = int(input("How many would you like ? : "))

Total = price * quantity
print(f"You have bought {quantity} x {item} ")
print(f"The total of {item} is {Total} ")