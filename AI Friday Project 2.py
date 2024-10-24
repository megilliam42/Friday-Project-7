import random
import time

def generate_powerball_numbers():
    print("Welcome to the PowerBall Number Generator!")
    print("This program will generate your lottery numbers for you.")

    # Generate five random white ball numbers between 1 and 69
    white_balls = []
    for _ in range(5):
        number = random.randint(1, 69)
        white_balls.append(number)
        # Optional delay for extra practice
        time.sleep(0.5)

    # Generate one random red ball number between 1 and 26
    red_ball = random.randint(1, 26)

    # Print the numbers with the specified format
    print("\nYour PowerBall numbers are:")
    print(" ".join(map(str, white_balls)), "   ", red_ball)

    print("\nGood luck, and have a great day!")

if __name__ == "__main__":
    generate_powerball_numbers()