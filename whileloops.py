# while loop = execute some code WHILE some condition remains true

#example 1
name = input("Enter your name : ")

while name == "":
    print("You did not enter a name ")
    name = input("Enter your name : ")
print(f"Hello {name}")


# example 2
age = int(input("Enter your age: "))

while age<0:
    print("Age can not be negative")
    age = int(input("Enter your age: "))
print(f"your age is {age}")

#example 3 with quit
food = input("Enter a food you like (q to quit) : ")

while not food =="q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit) : ")
print("bye")