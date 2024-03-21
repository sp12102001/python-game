import random
import time
from math_question_generator import generate_math_question, increase_difficulty
from scoring_system import calculate_score

# ANSI escape codes for colors and styles
ANSI_CYAN = '\033[96m'
ANSI_GREEN = '\033[92m'  # Green for correct answers by the human player
ANSI_YELLOW = '\033[93m'
ANSI_MAGENTA = '\033[95m'  # Magenta for incorrect answers by the computer
ANSI_RED = '\033[91m'  # Red for incorrect answers by the human player
ANSI_BLUE = '\033[94m'  # Blue for correct answers by the computer
ANSI_RESET = '\033[0m'
ANSI_BOLD = '\033[1m'

def computer_play(difficulty_level):
    accuracy_threshold = max(0.2, 0.75 - (difficulty_level * 0.03))
    is_correct = random.random() < accuracy_threshold
    thinking_time = random.uniform(0.5, 2.0)
    return is_correct, thinking_time

def main():
    print(ANSI_CYAN + "Welcome to the Maths Quiz Game!" + ANSI_RESET)
    if input("Do you want to play the game? (y/n): ").lower() != 'y':
        print("Maybe next time!")
        return

    player_name = input("What's your name? ")
    print(f"Hi {ANSI_BOLD}{player_name}{ANSI_RESET}, let's start the quiz!")

    total_score, total_computer_score, difficulty_level = 0, 0, 1

    while True:
        question, correct_answer = generate_math_question(difficulty_level)
        computer_correct, computer_thinking_time = computer_play(difficulty_level)

        print(f"Question: {question}")
        start_time = time.perf_counter()
        player_answer = input("Your answer (within 10 seconds): ")
        end_time = time.perf_counter()

        try:
            player_answer = int(player_answer)
            player_correct = correct_answer == player_answer
        except ValueError:
            print(ANSI_RED + "Invalid number. Skipping to the next question." + ANSI_RESET)
            continue

        time_taken = end_time - start_time
        if player_correct:
            print(ANSI_GREEN + "Correct!" + ANSI_RESET)
            score = calculate_score(correct_answer, player_answer, time_taken)
        else:
            print(ANSI_RED + f"Incorrect. The correct answer was: {correct_answer}." + ANSI_RESET)
            score = 0

        total_score += score
        print(f"Your score for this question: {score}")

        if computer_correct:
            computer_score = calculate_score(correct_answer, correct_answer, computer_thinking_time)
            print(ANSI_BLUE + "The computer was correct." + ANSI_RESET)
        else:
            computer_score = 0
            print(ANSI_MAGENTA + "The computer was incorrect." + ANSI_RESET)

        total_computer_score += computer_score
        print(f"Computer's score for this question: {computer_score}.")

        if input("Play another question? (y/n): ").lower() != 'y':
            break

        difficulty_level = increase_difficulty(difficulty_level) if player_correct else difficulty_level

    print(ANSI_CYAN + f"Game over! Your total score is {total_score}. Computer's total score is {total_computer_score}. Thank you for playing, {player_name}!" + ANSI_RESET)

if __name__ == "__main__":
    main()
