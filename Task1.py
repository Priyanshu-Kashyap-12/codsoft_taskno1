# Simple Calculator

# Introduction:
# In this program, we will create a basic calculator that takes two numbers and an operator as input and
# performs the chosen arithmetic operation.
# It also allows the user to perform multiple calculations.'''

start = 1
while start > 0:
    
    # 2. Taking input from the user:
    # Explain in the video that the program asks for two numbers and an operator.
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Choose operator(+,-,*,/): ")

    # 3. Performing calculations:
    # Highlight how different conditions handle specific operations (+, -, *, /).
    if operator == "+":
        print(f"Result of {num1} + {num2} is {num1 + num2}")
    elif operator == "-":
        print(f"Result of {num1} - {num2} is {num1 - num2}")
    elif operator == "*":
        print(f"Result of {num1} * {num2} is {num1 * num2}")
    elif operator == "/":
        if num2 != 0:
            print(f"Result of {num1} / {num2} is {num1 / num2}")
        else:
            print("Don't enter second number '0'!")  # Error handling for division by zero.
    else:
        print("Please enter valid Operator!")  # Handles invalid operator input.

    # 4. Conclusion:
    # Demonstrate how the program allows users to perform multiple calculations 
    # or exit the loop by entering 'n'.
    choice = input("For stopping here enter 'n', and for doing more calculations enter any other key: ")
    if choice == "n":
        break
    start += 1

# End of the program
# Conclusion in the video: This calculator is a basic implementation of arithmetic operations
# and uses loops for multiple executions.
