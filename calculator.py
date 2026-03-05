import math

# Simple Four-Function Calculator
while True:
    print("--- Python Console Calculator ---")
    print("Select operation: +, -, *, /, %, //, sqrt, quit,!")

    # 1. Take user input for the operation
    operation = input("Enter operation: ")

    if operation == 'quit':
        print("Exiting calculator. Goodbye!")
        break

    # 2. Take user input for numbers (converted to floats)
    raw = input("Enter first number (or 'quit' to exit): ")
    if raw.strip().lower() == 'quit':
        print("Exiting calculator. Goodbye!")
        break
    try:
        num1 = float(raw)
    except ValueError:
        print("Invalid number.")
        continue

    if operation not in ('sqrt', '!'):
        raw2 = input("Enter second number (or 'quit' to exit): ")
        if raw2.strip().lower() == 'quit':
            print("Exiting calculator. Goodbye!")
            break
        try:
            num2 = float(raw2)
        except ValueError:
            print("Invalid number.")
            continue

    # 3. Perform the calculation based on the operation
    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")

    elif operation == '!':
        total = 1
        if num1 < 0 or not num1.is_integer():
            print("Error: must be positive integer.")
        else:
            for i in range(2, int(num1) + 1):
                total *= i
            print(f'{int(num1)}! = {total}')
    
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")

    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")

    elif operation == '/':
        # Check for division by zero
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Cannot divide by zero.")

    elif operation == '%':
        result = num1 % num2
        print(f"{num1} % {num2} = {result}")

    elif operation == '//':
        result = num1 // num2
        print(f"{num1} // {num2} = {result}")

    elif operation == 'sqrt':
        if num1 >= 0:
            result = math.sqrt(num1)
            print(f"sqrt({num1}) = {result}")
        else:
            print("Error: Cannot take square root of negative number.")

    else:
        print("Invalid operation selected.")