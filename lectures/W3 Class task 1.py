#!/usr/bin/env python3

if __name__ == '__main__':
    
    marks = []

    # Read five marks from the user
    for i in range(5):
        mark = float(input(f"Enter mark {i + 1} (0-100): "))
        marks.append(mark)

    # Calculate highest, lowest, and mean
    highest = max(marks)
    lowest = min(marks)
    mean = sum(marks) / len(marks)

    # Output the results
    print(f"Highest mark: {highest}")
    print(f"Lowest mark: {lowest}")
    print(f"Mean mark: {mean:.2f}")