# match case statement (switch) : An alternative to using many elif statements
#                                 Executes some code if a value matches a 'case'
#                                 Benefits: cleaner and syntax is more readable


def day_of_week(day):
    match day:# case name is day
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _: #wildcard like an else statement if not from the case(1-7)
            return "Not a valid day"
    
day=int(input("enter days of the week (1-7) : "))
print(day_of_week(day))