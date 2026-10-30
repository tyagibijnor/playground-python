# Conditional example in Python

age = 18

# if statement
if age >= 18:
    print("You are an adult")

# if-else statement
if age < 13:
    print("You are a child")
else:
    print("You are a teenager or adult")

# if-elif-else statement
if age < 13:
    print("You are a child")
elif age < 18:
    print("You are a teenager")
else:
    print("You are an adult")

# Nested conditionals
score = 85

if score >= 60:
    if score >= 80:
        print("Grade: A")
    elif score >= 70:
        print("Grade: B")
    else:
        print("Grade: C")
else:
    print("Failed")

# Conditional with logical operators
temperature = 25

if temperature > 20 and temperature < 30:
    print("Weather is pleasant")
elif temperature >= 30:
    print("It's hot")
else:
    print("It's cold")
    
## input and conditional
user_input = input("Enter your age: ") # This will prompt the user to enter their age and store it as a string in the variable user_input
age = int(user_input) # This will convert the user input from a string to an integer and store it in the variable age
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

## nested if-else with user input
score_input = input("Enter your score: ") # This will prompt the user to enter their score and store it as a string in the variable score_input
score = int(score_input) # This will convert the user input from a string to an integer and store it in the variable score
if score >= 60:
    if score >= 80:
        print("Grade: A")
    elif score >= 70:
        print("Grade: B")
    else:
        print("Grade: C")
else:
    print("Failed")

## calculator with conditional
num1_input = input("Enter the first number: ") # This will prompt the user to enter the first number and store it as a string in the variable num1_input
num2_input = input("Enter the second number: ") # This will prompt the user to  enter the second number and store it as a string in the variable num2_input
num1 = float(num1_input) # This will convert the user input from a string to a float and store it in the variable num1
num2 = float(num2_input) # This will convert the user input from a string to a float and store it in the variable num2
operation = input("Enter the operation (+, -, *, /): ") # This will prompt the user to enter the operation they want to perform and store it as a string in the variable operation
if operation == "+":    
    result = num1 + num2
    print("Result:", result)
elif operation == "-":
    result = num1 - num2
    print("Result:", result)
elif operation == "*":
    result = num1 * num2
    print("Result:", result)    
elif operation == "/":
    result = num1 / num2
    print("Result:", result)    
else:
    print("Invalid operation")

## leap year checker
year_input = input("Enter a year: ") # This will prompt the user to enter a year and store it as a string in the variable year_input
year = int(year_input) # This will convert the user input from a string to an integer and store it in the variable year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

## recursion with conditional
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) # This will define a recursive function that calculates the factorial of a number n using conditional statements to check for the base case and the recursive case  
print("Factorial of 5:", factorial(5)) # This will call the factorial function with the argument 5 and print the result         
    