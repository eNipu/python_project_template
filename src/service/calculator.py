import math

# This is the calculator class
class Calculator:
    # This is the constructor
    def __init__(self):
        self.result = 0

    # This is the add method
    def add(self, num1, num2):
        self.result = num1 + num2
        return self.result

    # This is the subtract method
    def subtract(self, num1, num2):
        self.result = num1 - num2
        return self.result
    
    # This is the multiply method
    def multiply(self, num1, num2):
        self.result = num1 * num2
        return self.result

    # This is the divide method
    def divide(self, num1, num2):
        self.result = num1 / num2
        return self.result
    
    # This is the square root method
    def square_root(self, num1):
        self.result = math.sqrt(num1)
        return self.result

    # This is the square method
    def square(self, num1):
        self.result = num1 ** 2
        return self.result

    # This is the cube method
    def cube(self, num1):
        self.result = num1 ** 3
        return self.result

    # This is the power method
    def power(self, num1, num2):
        self.result = num1 ** num2
        return self.result

    # This is the modulus method
    def modulus(self, num1, num2):
        self.result = num1 % num2
        return self.result

    # This is the logarithm method
    def logarithm(self, num1):
        self.result = math.log(num1)
        return self.result

    # This is the sine method
    def sine(self, num1):
        self.result = math.sin(num1)
        return self.result

    # This is the cosine method
    def cosine(self, num1):
        self.result = math.cos(num1)
        return self.result

    # This is the tangent method
    def tangent(self, num1):
        self.result = math.tan(num1)
        return self.result
