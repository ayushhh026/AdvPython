# default arguments = A default value for certain arameters
#                     default is used when that argument is omitted
#                     make your functions more flexible,
#                     reduces # of arguments
#                     1.positional done in functions.py 2.DEFAULT 3.keyword 4. arbitrary

# 2.DEFAULT arguments
def net_price(list_price,discount= 0,tax = 0.05): # these are default value of discount which will be taken if no value given
    return list_price * (1-discount)*(1+ tax)

#print(net_price(500)) this will not work as other 2 arguments not given

 # to print like this use default values for discount and tax
  
print(net_price(500))

print(net_price(500,0.1))

