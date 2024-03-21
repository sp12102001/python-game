import random

def generate_question(difficulty):
    operations = ['+', '-', '*', '/']  # Keep all operations, including division
    operation = random.choice(operations)

    if operation == '/':
        # For division, ensure whole number results by making sure num1 is divisible by num2
        num2 = random.randint(1, 10 + difficulty * 2)
        divisors = [i for i in range(1, 10 + difficulty * 2) if i % num2 == 0]
        num1 = random.choice(divisors)
    else:
        # For other operations, generate any random numbers within the adjusted difficulty range
        num1 = random.randint(1, 10 + difficulty * 5)
        num2 = random.randint(1, 10 + difficulty * 5)

    # Formulate the question and calculate the answer
    question = f"What is {num1} {operation} {num2}?"
    correct_answer = int(eval(f"{num1} {operation} {num2}"))  # Use int() to ensure the answer is a whole number

    return question, correct_answer
