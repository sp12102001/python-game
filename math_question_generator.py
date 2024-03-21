import random

def generate_math_question(difficulty_level):
    operations = ['+', '-', '*', '/']
    operation = random.choice(operations)
    
    if operation == '/':
        num1 = random.randint(1, 10 + difficulty_level * 5)
        num2 = random.choice([i for i in range(1, num1 + 1) if num1 % i == 0])
    else:
        num1 = random.randint(1, 10 + difficulty_level * 5)
        num2 = random.randint(1, 10 + difficulty_level * 5)

    question = f"What is {num1} {operation} {num2}?"
    correct_answer = int(eval(f"{num1} {operation} {num2}"))

    return question, correct_answer

def increase_difficulty(current_difficulty):
    return current_difficulty + 1
