import random 

number = random.randint(1,6) # this gives random intger from 1 to 6
print(number)
 
low=1
high=100 
no = random.randint(low,high)
print(no)

options = ("rock", "paper", "scissors")
option = random.choice(options)
print(option)