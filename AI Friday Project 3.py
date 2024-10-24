import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    play = input("Do you want to play? (yes/no): ").strip().lower()

    if play == "yes":
        secret_number = random.randint(1, 10)
        guessed_correctly = False

        print("I'm thinking of a number between 1 and 10.")

        while not guessed_correctly:
            guess = int(input("Please enter your guess: "))

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print("Congratulations! You've guessed the number!")
                guessed_correctly = True
        
    else:
        print("Maybe next time!")

    print("Thanks for playing! Have a great day!")

if __name__ == "__main__":
    number_guessing_game()