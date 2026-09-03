'''num1 = float(input("enter first number"))
num2 = float(input("enter second number"))
operation = input("Choose operation(+, -, *, /): ")
if operation == "+":
    print("Result =", num1 + num2)
elif operation == "-":
    print("Result =", num1 - num2) 
elif operation == "*":
    print("Result =", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("0 se divide nahi kar sakte")
else:
    print("Galat operation")'''




# Simple Calculator using try-except

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