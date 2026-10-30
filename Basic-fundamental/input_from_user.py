## Testing user input case
name=input("Enter your name : ")
print(' Welcome ',name) 
print(type(name))
## Math operations
def arithmetic_operation():
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            result = num1 / num2
        else:
            return "Invalid operator."

        return f"The result of {num1} {operator} {num2} is {result}"

    except ValueError:
        return "Invalid input. Please enter numeric values."

print(arithmetic_operation())
