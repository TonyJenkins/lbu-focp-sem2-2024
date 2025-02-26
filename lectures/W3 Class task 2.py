
# #!/usr/bin/env python3

# if __name__ == '__main__':

#     p = input("Enter a password: ")
#     p1 = input("Confirm your password again: ")

#     if (p == p1 and 8 <= len(p) <= 12 and any(c.isupper() for c in p) and any(c.islower() for c in p) 
#         and any(c.isdigit() for c in p) and any(c in '!@#$%^&*()-_=+[]{}|;:,.<>?/' for c in p)):
#         print("Thanks!! Password Set")
#     else:
#         print("Invalid password: Must be 8-12 characters long, contain uppercase, lowercase, a digit, and a special character.")
# Problem 10: University Password Validation
p = input("Enter a password: ")
p1 = input("Confirm your password again: ")

if p != p1:
    print("Error: Passwords do not match.")
elif not (8 <= len(p) <= 12):
    print("Error: Password must be between 8 and 12 characters long.")
elif not any(c.isupper() for c in p):
    print("Error: Password must contain at least one uppercase letter.")
elif not any(c.islower() for c in p):
    print("Error: Password must contain at least one lowercase letter.")
elif not any(c.isdigit() for c in p):
    print("Error: Password must contain at least one digit.")
elif not any(c in '!@#$%^&*()-_=+[]{}|;:,.<>?/' for c in p):
    print("Error: Password must contain at least one special character.")
else:
    print("Thanks!! Password Set")
