def calculate_score(correct_answer, player_answer, time_taken, time_limit=10):
    if correct_answer == player_answer:
        score = max(0, time_limit - time_taken)
        return round(score, 2)
    else:
        return 0
