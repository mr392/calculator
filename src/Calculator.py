def addition(a, b):

    return a + b

def subtraction(a, b):
    return b - a




class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(int(a), int(b))
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result