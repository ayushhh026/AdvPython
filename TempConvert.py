unit = input("Is the temperature in Celsius(C) or Fahrenheit(F) : ")
temp = float(input("Enter the temperature : "))

if unit == "C":
    temp = round((9* temp)/5 +31,2)
    print(f"The temeperature in Fahreheit is {temp}°F")# to get °  >> numlock on press at + 0 1 7 6 in numpad
elif unit == "F":
    temp = round((temp - 32) *5/9,2)
    print(f"The temeperature in Celcisus is {temp}°C")
else:
    print(f"{unit} is an invalid unit of measurement")