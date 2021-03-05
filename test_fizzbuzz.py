import unittest
from fizzbuzz import fizzbuzz

class TestFizzbuzz(unittest.TestCase):
  def test_fizzBuzzInvalid(self):
    self.assertEqual(fizzbuzz(-1), None)
  def test_fizzBuzz3(self):
    self.assertEqual(fizzbuzz(3), "Fizz")
  
if __name__ == "__main__":
    unittest.main()