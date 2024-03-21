def calculate_score(correct_answer, player_answer, time_taken, time_limit=10):
    """
    Calculates the score for a given answer based on correctness and time taken.

    Parameters:
    - correct_answer: The correct answer to the question.
    - player_answer: The answer provided by the player.
    - time_taken: The time taken by the player to answer the question, in seconds.
    - time_limit: The maximum time allowed to answer the question, in seconds (default is 10).

    Returns:
    - The score awarded for the question. Full score if correct and within time limit, 
      otherwise proportional to the time remaining, and 0 for incorrect answers.
    """
    if correct_answer == player_answer:
        # Calculate score based on time efficiency (the quicker the response, the higher the score)
        score = max(0, time_limit - time_taken)
        return round(score, 2)
    else:
        return 0