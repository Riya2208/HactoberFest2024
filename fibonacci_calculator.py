# fibonacci_calculator.py
# GitHub Username: Riya2208
# Aim: To create a Fibonacci series calculator using classes.
# Date: 2024-10-07

class FibonacciCalculator:
    def __init__(self, count):
        self.count = count

    def calculate_fibonacci(self):
        fib_sequence = []
        a, b = 0, 1
        for _ in range(self.count):
            fib_sequence.append(a)
            a, b = b, a + b
        return fib_sequence

if __name__ == "__main__":
    n = 10  # Change this value to generate more numbers
    calculator = FibonacciCalculator(n)
    print(f"Fibonacci series up to {n}: {calculator.calculate_fibonacci()}")
