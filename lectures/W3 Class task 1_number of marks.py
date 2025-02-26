#!/usr/bin/env python3

if __name__ == '__main__':
    
    marks = []
    number_of_marks = int(input("Enter how many number of marks you want:"))

   
    for i in range(number_of_marks):                               # Read marks from the user
        mark = float(input(f"Enter mark {i + 1} (0-100): "))
        marks.append(mark)

    
    highest = max(marks)                     # Calculate highest, lowest, and mean
    lowest = min(marks)
    mean = sum(marks) / len(marks)

    # Output the results
    print(f"Highest mark: {highest}")
    print(f"Lowest mark: {lowest}")
    print(f"Mean mark: {mean:.2f}")