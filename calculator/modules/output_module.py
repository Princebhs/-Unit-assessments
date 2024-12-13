# modules/output_module.py

def print_result(operation, num1, num2, result):
    """Prints the result of the calculation."""
    print(f"The {operation} between {num1} and {num2} is {result}")

def append_to_file(operation, num1, num2, result):
    """Appends the result to calculations.txt."""
    with open("calculations.txt", "a") as file:
        file.write(f"The {operation} between {num1} and {num2} is {result}\n")
