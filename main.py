#Main Game Logic

import time
import random
from math_question_generator import generate_math_question
from scoring_system import calculate_score

def main():
    print("Welcome to the Maths Quiz Game!")
    if input("Do you want to play the game? (yes/no): ").lower() != 'yes':
        print("Maybe next time!")
        return

    player_name = input("What's your name? ")
    print(f"Hi {player_name}, let's start the quiz!")

    total_score = 0
    continue_playing = True

    while continue_playing:
        question, correct_answer = generate_math_question()
        print(f"Question: {question}")
        start_time = time.time()
        player_answer = float(input("Your answer: "))
        end_time = time.time()

        time_taken = round(end_time - start_time, 2)
        score = calculate_score(correct_answer, player_answer, time_taken)
        total_score += score

        print(f"Your score for this question: {score}")
        if input("Play another question? (yes/no): ").lower() != 'yes':
            continue_playing = False

    print(f"Game over! Your total score is {total_score}. Thank you for playing, {player_name}!")

if __name__ == "__main__":
    main() 