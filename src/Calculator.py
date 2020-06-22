from math import sqrt




def subtraction(a, b):
    return b - a

def multiplication(a, b):
    return a * b

def division(a, b):
    return b / a

def squared(a):
    return  a * a

def square_root_of_number(a):
    return sqrt(a)



class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = Calculator.addition(int(a), int(b))
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a,b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a,b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = squared(a)
        return self.result

    def square_root(self, a):
        self.result = square_root_of_number(a)
        return self.result

    @staticmethod
    def addition(a, b):
        return a + b
