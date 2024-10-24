import random

# Function to return colored text
def redText(text):
    return f"\033[31m{text}\033[0m"

def blueText(text):
    return f"\033[34m{text}\033[0m"

def greenText(text):
    return f"\033[32m{text}\033[0m"

def yellowText(text):
    return f"\033[33m{text}\033[0m"

def brownText(text):
    return f"\033[38;5;94m{text}\033[0m"  # Using ANSI code for brown

# Function for random color
def randomColor(text):
    colors = [redText, blueText, greenText, yellowText, brownText]
    return random.choice(colors)(text)

# Main program logic
def main():
    print("Choose a color to display your text:")
    print("1. Red")
    print("2. Blue")
    print("3. Green")
    print("4. Yellow")
    print("5. Brown")
    print("6. Random Color")
    print("7. Custom ANSI Color Code")
    
    while True:
        choice = input("Enter a number (1-7) or 'exit' to quit: ")

        if choice.lower() == 'exit':
            print("Goodbye!")
            break
        
        text = input("Enter your text: ")

        if choice == '1':
            print(redText(text))
        elif choice == '2':
            print(blueText(text))
        elif choice == '3':
            print(greenText(text))
        elif choice == '4':
            print(yellowText(text))
        elif choice == '5':
            print(brownText(text))
        elif choice == '6':
            print(randomColor(text))
        elif choice == '7':
            ansi_code = input("Enter your custom ANSI color code (e.g., 31 for red): ")
            print(f"\033[{ansi_code}m{text}\033[0m")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()