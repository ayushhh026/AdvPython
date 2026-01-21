# PYHTON compound INTEREST calculator
# final amount = principal_amount(1 +(rate/100) )^ time period

principle = 0 
rate = 0
time = 0

while principle <=0:
    principle = float(input("Enter the principle amount: "))
    if principle <=0:
        print("principle amount cant be that less than or equal to 0")

while rate <=0:
    rate = float(input("Enter the interest rate : "))
    if rate <=0:
        print("Interest rate amount cant be that less than or equal to 0")

while time <=0:
    time = int(input("Enter the Time in year : "))
    if time <=0:
        print("Time cant be that less than or equal to 0")

total = principle * pow(1+rate/100,time)
print(f"Compound interest for {principle} with rate of interest {rate} and time duration in year {time} is {round(total,3)}")