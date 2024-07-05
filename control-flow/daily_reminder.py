def get_user_input(message):
  """Prompts the user for input and returns the sanitized response."""
  while True:
    response = input(message).lower().strip()
    if response:
      return response
    else:
      print("Please enter a valid response.")

def main():
  # Get user input for task, priority, and time sensitivity
  task = get_user_input("Enter your task: ")
  priority = get_user_input("Priority (high/medium/low): ")
  time_bound = get_user_input("Is it time-bound? (yes/no): ")

  # Process task based on priority
  reminder = f"'{task}' is a "
  match priority:
    case "high":
      reminder += "high priority task"
    case "medium":
      reminder += "medium priority task"
    case "low":
      reminder += "low priority task"
    case _:
      print("Invalid priority level. Please enter high, medium, or low.")
      return

  # Modify reminder if time-bound
  if time_bound == "yes":
    reminder += " that requires immediate attention today!"
  else:
    reminder += ". Consider completing it when you have free time."

  # Print the reminder
  print(reminder)

if __name__ == "__main__":
  main()
