def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():

    first_num = float(input("What is the first number?: "))
    continue_calculating = "y"

    while continue_calculating == "y":

        for key in operations:
            print(key)
        operator = input("Pick an operation: ")
        second_number = float(input("What is the second number?: "))
        result = operations[operator](first_num, second_number)
        print(f"{first_num} {operator} {second_number} = {result}")
        first_num = result
        continue_calculating = input(
            f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: "
        )

    print("\n" * 10)
    calculator()


calculator()
