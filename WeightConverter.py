# Weight converter
#lbs to kg and vice versa

weight = float(input("Enter your weight ? : "))
unit= input("Kilogram(K) or Pounds(L) ? : ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Your unit is {unit} and weight is {round(weight,2)}")
elif unit == "L":
    weight =weight / 2.205
    unit = "Kg"
    print(f"Your unit is {unit} and weight is {round(weight,2)}")
else:
    print(f"{unit} not valid")

