
 #!/usr/bin/env python3

if __name__ == '__main__':
    import string

    def is_valid_password(password):
        if not (8 <= len(password) <= 12):
            return False
        
        has_upper = any(char.isupper() for char in password)
        has_lower = any(char.islower() for char in password)
        has_digit = any(char.isdigit() for char in password)
        has_special = any(char in string.punctuation for char in password)

        return all([has_upper, has_lower, has_digit, has_special])

    # Get password from user and check validity
    while True:
        password = input("Enter a password: ")

        if is_valid_password(password):
            print("Check Ok!")
        else:
            print("Check Failed! Password is invalid. ")

        break 



