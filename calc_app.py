def perform_calculation():
    """
    Perform a calculation based on user input.
    """
    try:
        num1 = float(input("Enter the first number: "))
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
        return

    operator = input("Enter the operator (+, -, *, /): ")

    try:
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
        return

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero.")
            return
        result = num1 / num2
    else:
        print("Error: Invalid operator.")
        return

    equation = f"{num1} {operator} {num2} = {result}"
    print("Result:", result)
    record_equation(equation)

def record_equation(equation):
    """
    Record the equation in the equations.txt file.
    """
    try:
        with open("equations.txt", "a", encoding='utf-8') as file:
            file.write(equation + "\n")
    except IOError:
        print("Error: Unable to write to file.")

def print_previous_equations():
    """
    Print all previously recorded equations.
    """
    try:
        with open("equations.txt", "r", encoding='utf-8') as file:
            equations = file.readlines()
            if equations:
                print("Previous equations:")
                for equation in equations:
                    print(equation.strip())
            else:
                print("No previous equations found.")
    except FileNotFoundError:
        print("No previous equations found.")
    except IOError:
        print("Error: Unable to read file.")

def calc_app():
    """
    Main calculator application loop.
    """
    while True:
        print("\nMenu:")
        print("1. Perform Calculation")
        print("2. Print Previous Equations")
        print("3. Exit")

        option = input("Enter your choice: ")

        if option == '1':
            perform_calculation()
        elif option == '2':
            print_previous_equations()
        elif option == '3':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    calc_app()



# Resources used for this task:
    
    # https://www.youtube.com/
    # https://www.google.com/
    # https://stackoverflow.com/questions/
    # https://www.cs50.net/
    # https://www.python.org/
    # https://www.w3schools.com/
    # Chat GPT