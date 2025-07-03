from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

mathematical_operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}

def calculator():
    first_num = float(input("What is the first number?: "))
    end_calculation = False
    number = first_num

    while not end_calculation:
        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        second_num = float(input("What is the next number?: "))
        result = mathematical_operations[operation](number, second_num)
        print(f"{number} {operation} {second_num} = {result}")
        should_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:\n").lower()

        if should_continue == "n":
            end_calculation = True
        elif should_continue == "y":
            number = result
        else:
            print("Type 'yes or no' to continue..")

    calculator()

calculator()