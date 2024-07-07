from datetime import datetime, timedelta

def display_current_datetime():
  """Gets the current date and time and prints it in a readable format."""
  current_date = datetime.now()
  formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
  print(f"Current date and time: {formatted_date}")

def calculate_future_date(days_to_add):
  """Calculates the future date based on the number of days added to the current date.

  Args:
      days_to_add: Number of days to add to the current date (integer).

  Returns:
      The future date in YYYY-MM-DD format.
  """
  current_date = datetime.now()
  future_date = current_date + timedelta(days=days_to_add)
  formatted_future_date = future_date.strftime("%Y-%m-%d")
  return formatted_future_date

if __name__ == "__main__":
  display_current_datetime()

  while True:
    try:
      days_to_add = int(input("Enter the number of days to add to the current date: "))
      future_date = calculate_future_date(days_to_add)
      print(f"Future date: {future_date}")
      break
    except ValueError:
      print("Invalid input. Please enter a number of days.")
