# match_case_calculator.py

def calculate(num1, num2, operator):
    match operator:
        case '+':
            result = num1 + num2
            print(f"The result is {result}.")
        case '-':
            result = num1 - num2
            print(f"The result is {result}.")
        case '*':
            result = num1 * num2
            print(f"The result is {result}.")
        case '/':
            if num2 != 0:
                result = num1 / num2
                print(f"The result is {result}.")
            else:
                print("Cannot divide by zero.")
        case _:
            print("Invalid operator entered.")

# Prompt user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ")

# Perform calculation based on operator
calculate(num1, num2, operator)
