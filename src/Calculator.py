from math import sqrt









class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = Calculator.addition(int(a), int(b))
        return self.result

    def subtract(self, a, b):
        self.result = Calculator.subtraction(a, b)
        return self.result

    def multiply(self, a,b):
        self.result = Calculator.multiplication(a, b)
        return self.result

    def divide(self, a,b):
        self.result = Calculator.division(a, b)
        return self.result

    def square(self, a):
        self.result = Calculator.squared(a)
        return self.result

    def square_root(self, a):
        self.result = Calculator.square_root_of_number(a)
        return self.result

    @staticmethod
    def addition(a, b):
        return a + b

    @staticmethod
    def subtraction(a, b):
        return b - a

    @staticmethod
    def multiplication(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        return b / a

    @staticmethod
    def squared(a):
        return a * a

    @staticmethod
    def square_root_of_number(a):
        return sqrt(a)
