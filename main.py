# ANSI escape codes for basic colors
ANSI_GREEN = '\033[92m'  # Green for correct answers by the human player
ANSI_RED = '\033[91m'  # Red for incorrect answers by the human player
ANSI_MAGENTA = '\033[95m'  # Magenta as a variant for incorrect answers by the computer
ANSI_BLUE = '\033[94m'  # Blue for correct answers by the computer
ANSI_RESET = '\033[0m'  # Reset to default terminal color

def main():
    print("Welcome to the Maths Quiz Game!")
    if input("Do you want to play the game? (y/n): ").lower() != 'y':
        print("Maybe next time!")
        return

    player_name = input("What's your name? ")
    print(f"Hi {player_name}, let's start the quiz!")

    total_score, total_computer_score, difficulty_level = 0, 0, 1

    while True:
        question, correct_answer = generate_math_question(difficulty_level)
        computer_correct, computer_thinking_time = computer_play(difficulty_level)

        print(f"Question: {question}")
        player_answer = input("Your answer (within 10 seconds): ")

        try:
            player_answer = int(player_answer)
            player_correct = correct_answer == player_answer
        except ValueError:
            print(ANSI_RED + "Invalid number. Skipping to the next question." + ANSI_RESET)
            continue

        if player_correct:
            print(ANSI_GREEN + "Correct!" + ANSI_RESET)
            score = calculate_score(correct_answer, player_answer, 0)  # Simplified
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

    print(f"Game over! Your total score is {total_score}. Computer's total score is {total_computer_score}. Thank you for playing, {player_name}!")

if __name__ == "__main__":
    main()
