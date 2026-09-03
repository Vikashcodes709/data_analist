'''1. write a program to build a calculater which will perform ?
(sabtaraction,addition,multiplication,divition).
a. input number into try block.
b. take a number an operters.
c. use except block to handel.'''


# Simple Calculator using try-except***

try:
    # Input two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Take an operator
    operator = input("Enter operator (+, -, *, /): ")

    # Perform calculation
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        print("Invalid operator!")
        result = None

    if result is not None:
        print("Result =", result)

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")