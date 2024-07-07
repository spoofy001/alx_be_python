def perform_operation(num1, num2, operation):
  """
  Performs basic arithmetic operations based on the provided parameters.

  Args:
      num1: First number (float).
      num2: Second number (float).
      operation: String representing the desired operation ('add', 'subtract', 'multiply', or 'divide').

  Returns:
      The result of the operation or a specific message for division by zero.
  """
  operation = operation.lower()  # Ensure case-insensitive operation handling
  if operation == 'add':
    return num1 + num2
  elif operation == 'subtract':
    return num1 - num2
  elif operation == 'multiply':
    return num1 * num2
  elif operation == 'divide':
    if num2 == 0:
      return "Error: Cannot divide by zero"
    else:
      return num1 / num2
  else:
    return "Invalid operation. Please enter 'add', 'subtract', 'multiply', or 'divide'."
