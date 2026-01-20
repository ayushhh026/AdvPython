import math

# calculate circumference of the circle = 2 * pi * radius

radius = float(input("Enter the Radius of a circle : "))

circumference = 2 * math.pi * radius
#round the decimal to  2 digits 
print(f"Circumference of the circle is {round(circumference,2)}")


# calculate area of circle = pi * radius **2 or pow(radius,2)

Area = math.pi * pow(radius,2)

print(f"Area of the Circle is : {round(Area,3)}")

#calculate hypoteneus of a right angle triangle c = sqrt((pow(a,2)+pow(b,2))

a = float(input("Enter a side of right angle triangle : "))
b = float(input("Enter another side of right angle triangle : "))

c = math.sqrt(pow(a,2) + pow(b,2))

print(f"The hypotenuse of the right angled triangle is {c}")
