# conditional expression = a one line shortcut for the if else statement (ternary operator)
# X if condition else Y

num = 5
numb = 12

print("Positive" if num > 0 else "Negative")

result = "Even" if num % 2 == 0  else "ODD"
print(result)

result = num if num>numb else numb

print(result)