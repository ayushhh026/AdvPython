#nested loop = A loop within another loop (outer,inner)
# outer loop:
#       inner loop:
for x in range(3):
    for i in range(1,10):
        print(i,end=" ")
         # by default the end="\n" which takes each number to next line we can change it like this
    print()

# code print a rectangle based on user rows and columns

rows = int(input("Enter the # of rows : "))
columns = int(input("Enter the # of columns : "))
symbol = input("Enter a symbol to use : ")

for x in range(rows):# you have to use range as the rows is in int
    for y in range(columns):
        print(symbol,end="")
    print()