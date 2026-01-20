# keyword arguments =  an argument preceded by an identifier helps with readablity
#                      order of arguments doesn't matter

def hello(greeting,title,first,last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello","Spongebob","Mr.","Squarepants") # this will give output as HelloSpongebobMr.Squarepants

# to get correct output use keyword arguments

hello(greeting="Hello",first="Spongebob",title="Mr.",last="Squarepants") # Hello Mr.Spongebob Squarepants

print("1","2","3","4",sep= " - ")# uses sep and seperate