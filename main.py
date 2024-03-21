import time
import random
from math_question_generator import generate_math_question, increase_difficulty
from scoring_system import calculate_score

def computer_play(difficulty_level):
    accuracy = random.uniform(0.5, 1.0) / difficulty_level
    simulated_time_taken = random.uniform(1, difficulty_level + 1)
    return accuracy >= 0.75, simulated_time_taken

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
        print(question)
        
        start_time = time.time()
        try:
            player_answer = int(input("Your answer: "))
        except ValueError:
            print("Please enter a valid number. You'll get the next one!")
            continue
        
        end_time = time.time()
        time_taken = round(end_time - start_time, 2)
        
        if player_answer == correct_answer:
            print("Correct!")
            score = calculate_score(correct_answer, player_answer, time_taken)
            total_score += score
            difficulty_level = increase_difficulty(difficulty_level)
        else:
            print(f"Incorrect. The correct answer was: {correct_answer}.")
            score = 0

        computer_correct, computer_time_taken = computer_play(difficulty_level)
        computer_score = calculate_score(correct_answer, 1 if computer_correct else 0, computer_time_taken)
        total_computer_score += computer_score
        
        print(f"Your score for this question: {score}. Computer's score for this question: {computer_score}.")
        
        if input("Play another question? (yes/no): ").lower() != 'yes':
            break

    print(f"Game over! Your total score is {total_score}. Computer's total score is {total_computer_score}. Thank you for playing, {player_name}!")

if __name__ == "__main__":
    main()
