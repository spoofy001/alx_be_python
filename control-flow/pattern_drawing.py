# pattern_drawing.py

# Prompt user for input
size = int(input("Enter the size of the pattern: "))

# Draw the pattern
row = 0
while row < size:
    column = 0
    while column < size:
        print("*", end="")
        column += 1
    print()  # Move to the next line after completing each row
    row += 1
