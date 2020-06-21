import unittest
import csv
from Calculator import Calculator


data = []
def csv_values(filename):

    data.clear()

    with open(filename) as text_data:

        reader = csv.DictReader(text_data, delimiter=",")

        for row in reader:
            data.append(row)

        return data




class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):

        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):

        self.assertEqual(self.calculator.result, 0)


    def test_add_method_calculator(self):
           addition_test_data = csv_values("/src/Unit Test Addition.csv")

           for number in addition_test_data:
             self.assertEqual(self.calculator.add(number['Value 1'], number['Value 2']), int(number['Result']))
             self.assertEqual(self.calculator.result, int(number['Result']))

    def test_subtract_method_calculator(self):
        subtraction_test_data = csv_values("/src/Unit Test Subtraction.csv")

        for number in subtraction_test_data:
            self.assertEqual(self.calculator.subtract(int(number['Value 1']), int(number['Value 2'])), int(number['Result']))
            self.assertEqual(self.calculator.result, int(number['Result']))

    def test_multiply_method_calculator(self):
        multiplication_test_data = csv_values("/src/Unit Test Multiplication.csv")

        for number in multiplication_test_data:
            self.assertEqual(self.calculator.multiply(int(number['Value 1']), int(number['Value 2'])), int(number['Result']))
            self.assertEqual(self.calculator.result, int(number['Result']))



if __name__ == '__main__':
   unittest.main()

