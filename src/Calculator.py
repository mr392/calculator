def subtraction (val1, val2):
    int(val1)
    int(val2)
    return  val1 - val2

class Calculator:
    result = 1

    def __init__(self):
        pass

    def subtract(self, a, b):
        a = 3
        b = 2
        self.result = subtraction(a, b)
