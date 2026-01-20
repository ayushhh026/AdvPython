#strings immutable data type (can not be changed once created) and its function
name = input("Enter your full name ")
#length of string len()
result = len(name)
print(result)

#string functions

#first occurence of given character index starts with 0
result = name.find(" ")
print(result)

#last occurence >> if it cant find it will return -1
result = name.rfind("t")
print(result)

#Capitalize first letter
result = name.capitalize()
print(result)

# all upper case
result= name.upper()
print(result)

# all lower case
result =name.lower()
print(result)

#if string contains only digit check with isdigit() give true or false
result = name.isdigit()
print(result)

#if string contains only Character check with isalpha() give true or false
result = name.isalpha()
print(result)


# count the number of something ina string
phone_number = input("Enter you phone number ")
result = phone_number.count("-")
print(result)

# replace with old and new .replace(old,new)

result = phone_number.replace("-","")
print(result)


# gives list of all the methods associated with the name variable which is string
print(dir(name))

# gives information and definition and how to use each method of string
print(help(str))


# Program to practice
#validate user
#1. username is no more than 12 characters
#2. username must not contain spaces
#3. username must not contain digits

username = input("Enter a username: ")
if len(username) >12:
    print("Your username cant be more than 12 characters")
elif not username.find(" ") == -1:
    print("User name consists of white space which are not allowed")
elif not username.isalpha():
    print("Your username cant contain numbers")
else:
    print(f"Welcome to the page {username}")