def add_two_numbers(a: int, b: int) -> int:
    """Adds two numbers and returns the result."""
    return a + b

def get_integer_from_user(prompt: str) -> int:
    """Prompts the user for an integer and keeps asking until valid input is received."""
    while True:
        try:
            user_input = input(prompt)
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def main():
    """A simple main function to greet the user and add two numbers."""
    print("Hello from the Python Demo project!")
    name = input("What is your name? ")
    print(f"Nice to meet you, {name}!")

    num1 = get_integer_from_user("Enter the first number: ")
    num2 = get_integer_from_user("Enter the second number: ")

    result = add_two_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()
