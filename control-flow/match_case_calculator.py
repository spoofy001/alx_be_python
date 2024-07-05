# match_case_calculator.py

def calculate(num1, num2, operator):
    result = match operator:
        case '+':
            num1 + num2
        case '-':
            num1 - num2
        case '*':
            num1 * num2
        case '/':
            num1 / num2 if num2 != 0 else None

    if result is None:
        print("Cannot divide by zero.")
    else:
        print(f"The result is {result}.")

# Prompt user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ")

# Perform calculation based on operator
calculate(num1, num2, operator)
