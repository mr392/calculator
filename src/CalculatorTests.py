import unittest
import csv
from Calculator import Calculator


data = []
def csv_values(filename):


    with open(filename) as text_data:

        reader = csv.DictReader(text_data, delimiter=",")

        for row in reader:
            values = data.append(row)

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

        self.assertEqual(self.calculator.subtract(2,2), 0)
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
   unittest.main()

