# assignment_while_loops.py
import random

def guessing_game():
    target_number = random.randint(1, 20)
    guess = None
    attempts = 0

    print("--- Welcome to the Number Guessing Game! ---")
    print("I'm thinking of a number between 1 and 20.")

    # Loop continues as long as the guess is incorrect
    while guess != target_number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! It took you {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

if __name__ == "__main__":
    guessing_game()