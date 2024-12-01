# Calculator
# from art import logo

# Addition
def add(n1, n2):
    return n1 + n2

# Subtraction
def subtract(n1, n2):
    return n1 - n2

# Multiplication
def multiply(n1, n2):
    return n1 * n2

# Division
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    num1 = float(input("What's the first number?: "))

    for operator in operations:
        print(operator)

    continue_calculation = True
    while continue_calculation:
        operator_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operator_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operator_symbol} {num2} = {answer} ")

        exit_calc = input(f"Type 'y' to continue calculation with {answer}, or 'n' to start a new calculation.: ")
        if exit_calc == "y":
            num1 = answer
        else:
            continue_calculation = False
            calculator()

calculator()