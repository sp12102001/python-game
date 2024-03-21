import random
from math_question_generator import generate_math_question, increase_difficulty
from scoring_system import calculate_score

def computer_play(difficulty_level):
    # Adjust accuracy based on difficulty; harder levels mean lower accuracy.
    accuracy_threshold = 0.75 - (difficulty_level * 0.05)
    # Determine if the computer gets the answer correct based on the accuracy threshold.
    is_correct = random.random() < accuracy_threshold
    # Simulate a random thinking time for the computer.
    thinking_time = random.uniform(0.5, 2.0)
    return is_correct, thinking_time

def main():
    # Greet the player at the beginning of the game.
    print("Welcome to the Maths Quiz Game!")
    # Ask the player if they want to play, expecting 'y' for yes or 'n' for no.
    if input("Do you want to play the game? (y/n): ").lower() != 'y':
        print("Maybe next time!")
        return  # Exit the game if the player does not want to play.

    # Ask for the player's name to personalize the experience.
    player_name = input("What's your name? ")
    print(f"Hi {player_name}, let's start the quiz!")

    # Initialize scores and difficulty level.
    total_score, total_computer_score, difficulty_level = 0, 0, 1

    while True:  # Start the main game loop.
        # Generate a new math question based on the current difficulty level.
        question, correct_answer = generate_math_question(difficulty_level)
        # Determine if the computer gets the question right and simulate thinking time.
        computer_correct, computer_thinking_time = computer_play(difficulty_level)

        # Display the question to the player.
        print(f"Question: {question}")
        # Record the time before the player starts typing their answer.
        start_time = time.perf_counter()
        player_answer = input("Your answer (within 10 seconds): ")
        # Record the time after the player submits their answer.
        end_time = time.perf_counter()

        try:  # Attempt to convert the player's answer to an integer.
            player_answer = int(player_answer)
            player_correct = correct_answer == player_answer
        except ValueError:  # Handle the case where the input is not a valid integer.
            print("Invalid number. Skipping to the next question.")
            player_correct = False

        # Calculate the time taken for the player to answer.
        time_taken = end_time - start_time
        if player_correct:  # If the player's answer is correct...
            print("Correct!")
            # Calculate the score for this question.
            score = calculate_score(correct_answer, player_answer, time_taken)
        else:  # If the player's answer is incorrect...
            print(f"Incorrect. The correct answer was: {correct_answer}.")
            score = 0  # No points are awarded.

        # Update the total score for the player.
        total_score += score
        print(f"Your score for this question: {score}")

        # Determine the computer's score for this question.
        if computer_correct:
            print("The computer was correct.")
            computer_score = calculate_score(correct_answer, correct_answer, computer_thinking_time)
        else:
            print("The computer was incorrect.")
            computer_score = 0

        # Update the total score for the computer.
        total_computer_score += computer_score
        print(f"Computer's score for this question: {computer_score}.")

        # Ask if the player wants to play another question.
        if input("Play another question? (y/n): ").lower() != 'y':
            break  # Exit the loop if the player does not want to continue.

        # Increase the difficulty level if the player got the answer right.
        difficulty_level = increase_difficulty(difficulty_level) if player_correct else difficulty_level

    # End of the game: display the final scores.
    print(f"Game over! Your total score is {total_score}. Computer's total score is {total_computer_score}. Thank you for playing, {player_name}!")

if __name__ == "__main__":
    main()
