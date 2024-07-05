# multiplication_table.py

# Prompt user for input
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print multiplication table
for i in range(1, 11):  # Loop from 1 to 10
    result = number * i
    print(f"{number} * {i} = {result}")
