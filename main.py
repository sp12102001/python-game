import random
from math_question_generator import generate_math_question, increase_difficulty
from scoring_system import calculate_score

def computer_play(difficulty_level):
    # Simulated computer thinking logic remains the same
    accuracy_threshold = 0.5 + 1.0 / (difficulty_level + 1)
    is_correct = random.random() < accuracy_threshold
    return is_correct

def main():
    print("Welcome to the Maths Quiz Game!")
    if input("Do you want to play the game? (yes/no): ").lower() != 'yes':
        print("Maybe next time!")
        return

    player_name = input("What's your name? ")
    print(f"Hi {player_name}, let's start the quiz!")

    total_score, total_computer_score, difficulty_level = 0, 0, 1

    while True:
        question, correct_answer = generate_math_question(difficulty_level)
        computer_correct = computer_play(difficulty_level)

        # Informing the player that the computer is "thinking"
        print("The computer is thinking...")
        
        print(f"Question: {question}")
        try:
            player_answer = int(input("Your answer (within 10 seconds): "))
        except ValueError:
            print("Please enter a valid number. You'll get the next one!")
            continue

        player_correct = correct_answer == player_answer
        
        if player_correct:
            print("Correct!")
            score = calculate_score(correct_answer, player_answer, 0)  # Adjusted time_taken to 0 for simplicity
            total_score += score
            difficulty_level = increase_difficulty(difficulty_level)
        else:
            print(f"Incorrect. The correct answer was: {correct_answer}.")

        # Simulate computer's score update
        computer_score = calculate_score(correct_answer, correct_answer if computer_correct else 0, 0)  # Assuming instant response for simplicity
        total_computer_score += computer_score
        print(f"Computer was {'correct' if computer_correct else 'incorrect'}.")

        print(f"Your score for this question: {score}. Computer's score for this question: {computer_score}.")

        if input("Play another question? (yes/no): ").lower() != 'yes':
            break

    print(f"Game over! Your total score is {total_score}. Computer's total score is {total_computer_score}. Thank you for playing, {player_name}!")

if __name__ == "__main__":
    main()
