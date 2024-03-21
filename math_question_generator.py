import random

def generate_math_question(difficulty_level):
    operations = ['+', '-', '*', '/', '**'] if difficulty_level > 2 else ['+', '-', '*', '/']
    operation = random.choice(operations)

    max_num = 10 + (difficulty_level * 5)  # Increase the range of numbers as difficulty increases
    num1 = random.randint(1, max_num)
    num2 = random.randint(1, max_num)
    
    if operation == '/':
        while num2 == 0:
            num2 = random.randint(1, max_num)
    elif operation == '**':
        num2 = random.randint(1, 3)  # Keep exponent small for simplicity

    question = f"{num1} {operation} {num2}"
    correct_answer = round(eval(question), 2)

    return question, correct_answer

def increase_difficulty(level):
    return level + 1
