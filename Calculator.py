# PYTHON CALCULATOR USING ONLY IF CONDITIONS

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st Number : ")) # REMEMBER TO DO TYPE CASTING str() to float()
num2 = float(input("Enter the 2nd Number : "))

if operator == "+":
    result= num1 + num2
    print(f"Result is {round(result,2)}")
elif operator == "-":
    result= num1 - num2
    print(f"Result is {round(result,2)}")
elif operator =="*":
    result= num1 * num2
    print(f"Result is {round(result,2)}")
elif operator == "/":
    result= num1 / num2
    print(f"Result is {round(result,2)}")
else:
    print("Invalid choice entered")