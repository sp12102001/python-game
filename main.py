import time
import random
from math_question_generator import generate_math_question, increase_difficulty
from scoring_system import calculate_score

def computer_play(difficulty_level):
    # Simulate computer's play: accuracy decreases and response time increases with difficulty
    accuracy = random.uniform(0.5, 1.0) / difficulty_level  # Decrease accuracy as difficulty increases
    simulated_time_taken = random.uniform(1, difficulty_level + 1)  # Increase time as difficulty increases
    return accuracy >= 0.75, simulated_time_taken  # Simplified: 75% chance of correct on easy level

def main():
    print("Welcome to the Maths Quiz Game!")
    
    if input("Do you want to play the game? (yes/no): ").lower() != 'yes':
        print("Maybe next time!")
        return

    player_name = input("What's your name? ")
    print(f"Hi {player_name}, let's start the quiz!")

    total_score, total_computer_score, difficulty_level = 0, 0, 1
    continue_playing = True

    while continue_playing:
        question, correct_answer = generate_math_question(difficulty_level)
        print(f"Question: {question}")
        
        start_time = time.time()
        try:
            player_answer = float(input("Your answer (within 10 seconds): "))
        except ValueError:
            print("Please enter a valid number. You'll get the next one!")
            continue
        
        end_time = time.time()
        time_taken = round(end_time - start_time, 2)
        player_correct = correct_answer == round(player_answer, 2)
        
        if player_correct:
            score = calculate_score(correct_answer, player_answer, time_taken)
            print(f"Correct! Your score for this question: {score}")
            total_score += score
            difficulty_level = increase_difficulty(difficulty_level)  # Increase difficulty after correct answer
        else:
            print(f"Incorrect. The correct answer was: {correct_answer}.")
            score = 0
        
        # Simulate computer's play
        computer_correct, computer_time_taken = computer_play(difficulty_level)
        computer_score = calculate_score(correct_answer, 1 if computer_correct else 0, computer_time_taken, 10)
        total_computer_score += computer_score
        print(f"Computer's score for this question: {computer_score}")
        
        if input("Play another question? (yes/no): ").lower() != 'yes':
            continue_playing = False

    print(f"Game over! Your total score is {total_score}. Computer's total score is {total_computer_score}. Thank you for playing, {player_name}!")

if __name__ == "__main__":
    main()
