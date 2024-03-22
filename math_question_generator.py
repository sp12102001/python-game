import random

def generate_math_question(difficulty_level, operations):
    operation = random.choice(operations)
    
    # Adjusted difficulty scaling for division questions
    if operation == '/':
        num1 = random.randint(1, 10) * difficulty_level
        num2 = random.randint(1, 10) * difficulty_level
        num1 *= num2  # Ensures the division result is an integer
    else:
        num1 = random.randint(1, 10 + difficulty_level * 5)
        num2 = random.randint(1, 10 + difficulty_level * 5)

    question = f"What is {num1} {operation} {num2}?"
    correct_answer = round(eval(f"{num1} {operation} {num2}"), 2) if operation == '/' else eval(f"{num1} {operation} {num2}")

    return question, correct_answer

def increase_difficulty(current_difficulty):
    return min(current_difficulty + 1, 3)  # Max difficulty level capped at 3
