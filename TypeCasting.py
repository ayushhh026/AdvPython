#Type Casting = the process of converting a variable from one data type to another str(),int(),float(),bool()

name = "Master Blaster"
age = 20
CGPA = 9.61
is_student = True

# To get to know the data type of your variable use type() function and print it

print(type(CGPA)) #<class 'float'>


#Convert data type using type cast

CGPA = int(CGPA) #Truncate the decimal points

print(CGPA)
print(type(CGPA))

age = float(age)
print(age)
print(type(age))