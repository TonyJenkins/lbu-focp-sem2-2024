# #!/usr/bin/env python3
if __name__ == '__main__':


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
