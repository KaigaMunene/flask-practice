import unittest
from app.calculator import Calculator
class TestCalculator(unittest.TestCase):
  def test_calculator_returns_correct_result(self):
    calc = Calculator()
    result = calc.add(2,2)
    self.assertEqual(4,result) # ensure our method behaves as expected

if __name__ == "__main__":
  unittest.main()