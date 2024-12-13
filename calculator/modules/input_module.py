# modules/input_module.py

def get_numbers():
    """Gets two numbers from the user."""
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return get_numbers()  # Prompt the user again if input is invalid
