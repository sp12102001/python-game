import time
import random
from math_question_generator import generate_math_question, increase_difficulty
from scoring_system import calculate_score

def computer_play(difficulty_level):
    accuracy_threshold = 0.5 + 1.0 / (difficulty_level + 1)
    is_correct = random.random() < accuracy_threshold
    simulated_time_taken = random.uniform(1, 3)  # Simulates computer thinking time
    return is_correct, simulated_time_taken

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
        
        # Simulate computer thinking before showing the question to the player
        computer_correct, computer_time_taken = computer_play(difficulty_level)
        time.sleep(computer_time_taken)  # Simulates computer "thinking" time
        
        print(f"Question: {question}")
        start_time = time.time()
        try:
            player_answer = int(input("Your answer (within 10 seconds): "))
        except ValueError:
            print("Please enter a valid number. You'll get the next one!")
            continue
        
        end_time = time.time()
        time_taken = round(end_time - start_time, 2)
        player_correct = correct_answer == player_answer
        
        if player_correct:
            score = calculate_score(correct_answer, player_answer, time_taken)
            total_score += score
            print(f"Correct! Your score for this question: {score}")
            difficulty_level = increase_difficulty(difficulty_level)
        else:
            print(f"Incorrect. The correct answer was: {correct_answer}.")
            score = 0

        # Reveal computer's attempt after player's answer
        if computer_correct:
            print("The computer got it right!")
            computer_score = calculate_score(correct_answer, correct_answer, computer_time_taken)
        else:
            print("The computer got it wrong!")
            computer_score = 0
        
        total_computer_score += computer_score
        print(f"Your score for this question: {score}. Computer's score for this question: {computer_score}.")

        if input("Play another question? (yes/no): ").lower() != 'yes':
            break

    print(f"Game over! Your total score is {total_score}. Computer's total score is {total_computer_score}. Thank you for playing, {player_name}!")

if __name__ == "__main__":
    main()
