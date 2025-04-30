class Factorial:

    # def __init__(self, num1):  # Constructor to initialize the number

    #     self.num1 = num1

    def factorial(num1):  # Factorial method now works with self.num1

        result = 1  # Initialized before the loop to store the product.

        for i in range(1, num1 + 1):

            result *= i

        return result

    def check_Prime(num):  # Prime check method added

        if num < 2:  # 0 and 1 are not prime numbers

            return False

        for i in range(2, int(num ** 0.5) + 1): # Check up to the square root of num1 and int to make it not show decimal values

            # Check if num1 is divisible by i 

            if num % i == 0:

                return False

        return True
 
    def display(num):  # Display method corrected

        print("Factorial of", num, "is", Factorial.factorial(num))

        if Factorial.check_Prime(num):

            print(f"{num} is a prime number.")

        else:

            print(f"{num} is not a prime number.")
 


Factorial.display(5)
