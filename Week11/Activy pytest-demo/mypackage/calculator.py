import math

class Calculator:
    def add(self, a, b):
        """Addition operation"""
        return a + b
    
    def subtract(self, a, b):
        """Subtraction operation"""
        return a - b
    
    def multiply(self, a, b):
        """Multiplication operation"""
        return a * b
    
    def divide(self, a, b):
        """Division operation"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, base, exponent):
        """Power operation"""
        return math.pow(base, exponent)
    
    def root(self, number, n=2):
        """Nth root operation (default is square root)"""
        if number < 0 and n % 2 == 0:
            raise ValueError("Even root of negative number is not real")
        return math.pow(number, 1/n)
    
    def sin(self, degrees):
        """Sine of angle in degrees"""
        return math.sin(math.radians(degrees))
    
    def cos(self, degrees):
        """Cosine of angle in degrees"""
        return math.cos(math.radians(degrees))
    
    def tan(self, degrees):
        """Tangent of angle in degrees"""
        # Handle undefined cases (90 + 180k degrees)
        if degrees % 90 == 0 and degrees % 180 != 0:
            raise ValueError("Tangent is undefined for this angle")
        return math.tan(math.radians(degrees))

def main():
    calc = Calculator()
    print("Engineering Calculator")
    print("Operations: +, -, *, /, pow, root, sin, cos, tan")
    print("Enter 'quit' to exit")
    
    while True:
        try:
            user_input = input("please input the operation you need to perform").strip().lower()
            if user_input == 'quit':
                break
            elif user_input in ['+', '-', '*', '/', 'pow', 'root', 'sin', 'cos', 'tan']:
                if user_input in ['+', '-', '*', '/']:
                    a = float(input("Enter first number: "))
                    b = float(input("Enter second number: "))
                    if user_input == '+':
                        print(f"Result: {calc.add(a, b)}")
                    elif user_input == '-':
                        print(f"Result: {calc.subtract(a, b)}")
                    elif user_input == '*':
                        print(f"Result: {calc.multiply(a, b)}")
                    elif user_input == '/':
                        print(f"Result: {calc.divide(a, b)}")
                elif user_input == 'pow':
                    base = float(input("Enter base: "))
                    exponent = float(input("Enter exponent: "))
                    print(f"Result: {calc.power(base, exponent)}")
                elif user_input == 'root':
                    number = float(input("Enter number: "))
                    n = int(input("Enter root degree (default is 2): ") or 2)
                    print(f"Result: {calc.root(number, n)}")
                elif user_input == 'sin':
                    degrees = float(input("Enter angle in degrees: "))
                    print(f"Result: {calc.sin(degrees)}")
                elif user_input == 'cos':
                    degrees = float(input("Enter angle in degrees: "))
                    print(f"Result: {calc.cos(degrees)}")
                elif user_input == 'tan':
                    degrees = float(input("Enter angle in degrees: "))
                    print(f"Result: {calc.tan(degrees)}")
        except ValueError:
            print("Invalid number or operation. Please try again.")
      

if __name__ == "__main__":
    main()