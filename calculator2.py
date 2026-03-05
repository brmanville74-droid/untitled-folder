# calculator3.py
# prompt: convert all the operations to independent functions
import math

# --- 1. Independent Operation Functions ---

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def power(a, b):
    return a ** b

def modulo(a, b):
    return a % b

def floor_divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a // b

def square_root(a):
    if a < 0:
        return "Error: Cannot take square root of a negative number."
    return math.sqrt(a)

def factorial(a):
    if a < 0 or not a.is_integer():
        return "Error: Factorial is only for non-negative integers."
    return math.factorial(int(a))

# --- 2. Main Program Loop ---

if __name__ == '__main__':
    while True:
        print("\n--- Python Console Calculator ---")
        print("Options: +, -, *, /, %, //, **, sqrt, !, quit")
        
        op = input("Enter operation: ").strip().lower()

        if op == 'quit':
            print("Goodbye!")
            break

        # try:
        # Get the first number for all operations
      # ...existing code...
        try:
            num1 = float(input("Enter first number: "))
        except ValueError:
            print("Error: Please enter a valid numeric value.")
            continue

        # Check if the operation only needs one number
        if op == 'sqrt':
            print(f"Result: {square_root(num1)}")
        elif op == '!':
            print(f"Result: {factorial(num1)}")
        
        # Operations that need two numbers
        else:
            num2 = float(input("Enter second number: "))
            
            if op == '+': 
                print(f"Result: {add(num1, num2)}")
            elif op == '-': 
                print(f"Result: {subtract(num1, num2)}")
            elif op == '*': 
                print(f"Result: {multiply(num1, num2)}")
            elif op == '/': 
                print(f"Result: {divide(num1, num2)}")
            elif op == '**': 
                print(f"Result: {power(num1, num2)}")
            elif op == '%': 
                print(f"Result: {modulo(num1, num2)}")
            elif op == '//': 
                print(f"Result: {floor_divide(num1, num2)}")
            else: 
                print("Invalid operation selected.")

        #except ValueError:
        #    print("Error: Please enter a valid numeric value.")