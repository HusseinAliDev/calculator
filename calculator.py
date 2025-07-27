def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error: Division by zero"

print("Welcome to Calculator. Type 'exit' to quit.")

while True:
    inp = input("Enter operation (e.g. 4 + 5): ")
    if inp == 'exit':
        break
    try:
        num1, op, num2 = inp.split()
        num1, num2 = float(num1), float(num2)
        if op == '+':
            result = add(num1, num2)
        elif op == '-':
            result = subtract(num1, num2)
        elif op == '*':
            result = multiply(num1, num2)
        elif op == '/':
            result = divide(num1, num2)
        else:
            result = "Unknown operation!"
        print("Result:", result)
    except Exception as e:
        print("Invalid input. Try again.", str(e))
