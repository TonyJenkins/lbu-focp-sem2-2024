#!/usr/bin/env python3

BAD_PASSWORDS = ['password', 'hello', 'letmein', 'sesame', 'justinbieber']
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 12

if __name__ == '__main__':

    password = input("Enter Password: ")
    check_password = input("Enter Password again: ")

    if password == check_password:
        if MIN_PASSWORD_LENGTH <= len(password) <= MAX_PASSWORD_LENGTH and password not in BAD_PASSWORDS:
            print("Password Changed Successfully")
        else:
            if password in BAD_PASSWORDS:
                print("Password is common")
            else:
                print(f"Password Length should be between {MIN_PASSWORD_LENGTH} to {MAX_PASSWORD_LENGTH}")
    else:
        print("Password doesn't match")
