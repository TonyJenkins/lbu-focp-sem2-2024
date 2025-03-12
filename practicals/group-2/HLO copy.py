import random

def choose_number():
    
    return random.randint(0, 100)

def main():
    
    MAX_ATTEMPTS = 10

    number_to_guess = choose_number()

    print("Computer has chosen a number between 0 and 100.")
    print(f"You have {MAX_ATTEMPTS} attempts to guess it.")

    attempts = 1

    while True:

        try:
            guess = int(input(f"Attempt {attempts}: Enter your guess: "))
            if not (0 <= guess <= 100):
                print("Please guess a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
        else:
            attempts += 1

            if guess < number_to_guess:
                print("Try Higher.")
            elif guess > number_to_guess:
                print("Try Lower.")
            elif attempts == MAX_ATTEMPTS:
                print(f"Sorry, you've used all your attempts! The number was {number_to_guess}.")
                break
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts!")
                break
    

if __name__ == "__main__":
    main()