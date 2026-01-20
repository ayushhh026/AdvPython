# Logical operators = evaluate multiple conditions
#                or = at least one condition must be true
#               and = both conditions must be True
#               not = inverts the conditions not False , not True
#OR example
temp = 31
is_raining = False

if temp >35 or temp <0 or is_raining :
    print("The outdoor event is canceled")
else:
    print("The outdoor event is still scheduled")

#and example
is_sunny = False

if temp >=28 and is_sunny:
    print("It is Sunny and Hot outside")
#not example
elif temp >=28 and not is_sunny:
    print("It is cloudy")
else:
    print("It is not Hot outside")