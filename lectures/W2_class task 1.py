#!/usr/bin/env python3

if __name__ == '__main__':

    # Read five exam marks from the user
    mark1 = float(input("Enter mark for exam 1 (0-100): "))
    mark2 = float(input("Enter mark for exam 2 (0-100): "))
    mark3 = float(input("Enter mark for exam 3 (0-100): "))
    mark4 = float(input("Enter mark for exam 4 (0-100): "))
    mark5 = float(input("Enter mark for exam 5 (0-100): "))

    # Store marks in a list
    marks = [mark1, mark2, mark3, mark4, mark5]

    # Calculate highest, lowest, and mean
    highest = max(marks)
    lowest = min(marks)
    mean = sum(marks) / len(marks)

    # Output the results
    print(f"Highest mark: {highest}")
    print(f"Lowest mark: {lowest}")
    print(f"Mean mark: {mean:.2f}")