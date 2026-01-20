#indexing = accessing string elements of a sequence using [] 
# [start : end : step] index always start with 0


credit_no= "1234-4324-5465-4434"
print(credit_no[0])

# first four digits  [start: end -1](end is exclusive)
print(credit_no[0:4]) # it would be like 0 to 4-1 index i.e 0-3
print(credit_no[:7])# if start is empty it is presumed the first index i.e 0
print(credit_no[4:])# if ending is empty it is presumed till the last index 
print(credit_no[-1])# if you need last character of the string
print(credit_no[-2])# if you need second last character and so on 
# if you need from start go for positive index and if you need from back start from negative index

print(credit_no[::2])# start from last printing every second character from the string 
# output will be 13-.... i.e it will print index 0 2 4 6 8
print(credit_no[::3])


# code to get last 4 digits of a credit card no
last4= credit_no[-4:]
print(f"XXXX-XXXX-XXXX-{last4}")

# code to reverse the credit number in a string

credit_no = credit_no[::-1]
print(credit_no)