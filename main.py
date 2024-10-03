import sys
from calculator import Calculator
from decimal import Decimal, InvalidOperation

def calculate_and_print(a, b, operation_name):
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

    try:
        a_decimal = Decimal(a)
        b_decimal = Decimal(b)
        operation_func = operation_mappings.get(operation_name)
        if operation_func:
            result = operation_func(a_decimal, b_decimal)
            print(f"The result of {a} {operation_name} {b} is equal to {result}")
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("An error occurred: Cannot divide by zero.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)
    
    _, a, b, operation_name = sys.argv
    calculate_and_print(a, b, operation_name)

if __name__ == '__main__':
    main()
