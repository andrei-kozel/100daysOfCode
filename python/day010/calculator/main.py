import art


# Add
def add(n1, n2):
    """Returns the sum of two given numbers"""
    return n1 + n2


# Subtract
def subtract(n1, n2):
    """Returns the subtraction of two given numbers"""
    return n1 - n2


# Multiply
def multiply(n1, n2):
    """Returns the multiplication of two given numbers"""
    return n1 * n2


# Divide
def divide(n1, n2):
    """Returns the division of two given numbers"""
    return n1 / n2


print(art.logo)
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    first_number = float(input("What's your first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operator = input("Pick an operation: ")
        second_number = float(input("What's your next number?: "))
        answer = operations[operator](first_number, second_number)
        print(f"{first_number} {operator} {second_number} = {answer} ")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ") == 'y':
            first_number = answer
        else:
            should_continue = False
            calculator()


calculator()
