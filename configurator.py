def choose_difficulty():
    print("Choose your difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    choice = input("Enter your choice (1/2/3): ").strip()
    return {"1": 1, "2": 2, "3": 3}.get(choice, 1)  # Defaults to 1 (Easy) if input is invalid

def choose_operations():
    print("Choose the types of operations you want to practice:")
    print("A. Addition (+)")
    print("S. Subtraction (-)")
    print("M. Multiplication (*)")
    print("D. Division (/)")
    print("All. All of the above")
    choices = input("Enter your choices separated by commas (e.g., A,S,M): ").upper().strip()
    operations = {
        "A": "+",
        "S": "-",
        "M": "*",
        "D": "/"
    }
    if "ALL" in choices:
        return ["+", "-", "*", "/"]
    else:
        selected_operations = [operations[choice] for choice in choices.split(",") if choice in operations]
        return selected_operations if selected_operations else ["+"]  # Defaults to ["+"] if input is invalid
