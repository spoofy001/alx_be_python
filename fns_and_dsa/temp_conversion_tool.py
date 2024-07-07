FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
  """Converts a temperature from Fahrenheit to Celsius.

  Args:
      fahrenheit: Temperature value in Fahrenheit (float).

  Returns:
      The temperature converted to Celsius (float).
  """
  celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
  return celsius

def convert_to_fahrenheit(celsius):
  """Converts a temperature from Celsius to Fahrenheit.

  Args:
      celsius: Temperature value in Celsius (float).

  Returns:
      The temperature converted to Fahrenheit (float).
  """
  fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
  return fahrenheit

def main():
  while True:
    try:
      temperature = float(input("Enter the temperature to convert: "))
      unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
      if unit == 'C':
        converted_temperature = convert_to_fahrenheit(temperature)
        unit_label = "°C"
        result_unit = "°F"
      elif unit == 'F':
        converted_temperature = convert_to_celsius(temperature)
        unit_label = "°F"
        result_unit = "°C"
      else:
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
      print(f"{temperature}{unit_label} is {converted_temperature:.2f}{result_unit}")
      break
    except ValueError as e:
      print(f"Error: {e}")

if __name__ == "__main__":
  main()
