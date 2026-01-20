# # for loops = execute a block of code a fixed number of times.
# # you can iterate over a range, string, sequence, etc

# #example 1
# for i in range(1, 11):# range(starting,ending-1,steps)ending is always exclusive
#     print(i)

# # reverse count

# for i in reversed(range(1,11)):
#     print(i)

# # with steps
# for i in range(1,11,2):
#     print(i)

# #iteration over a string
# credit_no = "1234-4566-4353-1188"

# for x in credit_no:
#     print(x)


# some helpfull keywoards

# 1. continue skips the current interation and continues with the next iteration in the loop
for x in range(1,21):
    if x==13:
        continue
    else:
        print(x) # this will print 1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20 ignoring 13

# 2. break breaks out of the loop 
for x in range (1,21):
    if x==7:
        break 
    else:
        print(x)# this will print 1,2,3,4,5,6 it will not print after that