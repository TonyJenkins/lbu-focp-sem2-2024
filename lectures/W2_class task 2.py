# Read temperature readings for the day
temp1 = input("Enter temperature at 8am (e.g., 20C or 68F): ")
temp2 = input("Enter temperature at 11am (e.g., 22C or 72F): ")
temp3 = input("Enter temperature at 2pm (e.g., 25C or 77F): ")
temp4 = input("Enter temperature at 5pm (e.g., 23C or 73F): ")
temp5 = input("Enter temperature at 8pm (e.g., 21C or 70F): ")


temps = [temp1_c, temp2_c, temp3_c, temp4_c, temp5_c]

# Calculate maximum, minimum, range, and average
maximum = max(temps)
minimum = min(temps)
temperature_range = maximum - minimum
average = sum(temps) / len(temps)

# Output the results
print(f"Maximum temperature: {maximum:.2f}C")
print(f"Minimum temperature: {minimum:.2f}C")
print(f"Temperature range: {temperature_range:.2f}C")
print(f"Average temperature: {average:.2f}C")