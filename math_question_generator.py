import random

def generate_math_question():
    # Define the operations
    operations = ['+', '-', '*', '/']
    operation = random.choice(operations)

    # Generate two random numbers
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    
    # Ensure num2 is not 0 when operation is division
    if operation == '/':
        while num2 == 0:
            num2 = random.randint(1, 10)

    # Generate the question string
    question = f"{num1} {operation} {num2}"

    # Calculate the correct answer
    correct_answer = eval(question)

    # Round the answer to 2 decimal places if necessary
    correct_answer = round(correct_answer, 2)

    return question, correct_answer
