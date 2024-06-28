def perform_calculation():
    """
    Perform a calculation based on user input.
    This function prompts the user to input two numbers and an operator (+, -, *, /, **, %), performs the specified calculation, and records the equation.
    """
    try:
        # Prompt the user for the first number and convert it to a float
        num1 = float(input("Enter the first number: "))
    except ValueError:
        # Handle invalid input
        print("Error: Invalid input. Please enter a valid number.")
        return

    # Prompt the user for the operator
    operator = input("Enter the operator (+, -, *, /, **, %): ")

    try:
        # Prompt the user for the second number and convert it to a float
        num2 = float(input("Enter the second number: "))
    except ValueError:
        # Handle invalid input
        print("Error: Invalid input. Please enter a valid number.")
        return

    # Perform the calculation based on the operator
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            # Handle division by zero
            print("Error: Division by zero.")
            return
        result = num1 / num2
    elif operator == '**':
        result = num1 ** num2
    elif operator == '%':
        if num2 == 0:
            # Handle division by zero in modulus operation
            print("Error: Division by zero.")
            return
        result = num1 % num2
    else:
        # Handle invalid operator
        print("Error: Invalid operator.")
        return

    # Format the equation as a string
    equation = f"{num1} {operator} {num2} = {result}"
    # Print the result of the calculation
    print("Result:", result)
    # Record the equation in the file
    record_equation(equation)

def record_equation(equation):
    """
    Record the equation in the equations.txt file.
    This function appends the given equation to a file named 'equations.txt'.
    """
    try:
        # Open the file in append mode and write the equation
        with open("equations.txt", "a", encoding='utf-8') as file:
            file.write(equation + "\n")
    except IOError:
        # Handle file writing errors
        print("Error: Unable to write to file.")

def print_previous_equations():
    """
    Print all previously recorded equations.
    This function reads and prints all equations stored in 'equations.txt'.
    """
    try:
        # Open the file in read mode
        with open("equations.txt", "r", encoding='utf-8') as file:
            equations = file.readlines()
            if equations:
                # Print each equation
                print("Previous equations:")
                for equation in equations:
                    print(equation.strip())
            else:
                # Handle case where there are no recorded equations
                print("No previous equations found.")
    except FileNotFoundError:
        # Handle case where the file does not exist
        print("No previous equations found.")
    except IOError:
        # Handle file reading errors
        print("Error: Unable to read file.")

def calc_app():
    """
    Main calculator application loop.
    This function presents a menu to the user, allowing them to perform calculations, print previous equations, or exit the program.
    """
    while True:
        # Print the menu options
        print("\nMenu:")
        print("1. Perform Calculation")
        print("2. Print Previous Equations")
        print("3. Exit")

        # Prompt the user to choose an option
        option = input("Enter your choice: ")

        if option == '1':
            # Perform a calculation
            perform_calculation()
        elif option == '2':
            # Print previous equations
            print_previous_equations()
        elif option == '3':
            # Exit the program
            print("Exiting the program...")
            break
        else:
            # Handle invalid menu choice
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    # Start the calculator application
    calc_app()

# Resources used for this task:
# 
# https://www.youtube.com/
# https://www.google.com/
# https://stackoverflow.com/questions/
# https://www.cs50.net/
# https://www.python.org/
# https://www.w3schools.com/
# Chat GPT
