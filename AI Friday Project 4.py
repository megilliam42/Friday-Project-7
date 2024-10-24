# Trivia questions dictionary
trivia_questions = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who wrote 'Romeo and Juliet'?": "Shakespeare",
    "What is the chemical symbol for water?": "H2O",
    "What year did the Titanic sink?": "1912"
}

# Loop through the dictionary
for question, correct_answer in trivia_questions.items():
    # Display the question
    print(question)
    
    # Prompt for user input
    user_answer = input("Your answer: ")
    
    # Check if the user's answer is correct
    if user_answer.strip().lower() == correct_answer.lower():
        print("Correct!\n")
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}\n")

print("Thank you for participating!")