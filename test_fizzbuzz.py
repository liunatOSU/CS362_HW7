import unittest
from fizzbuzz import fizzbuzz

class TestFizzbuzz(unittest.TestCase):
  def test_fizzbuzzInvalid(self):
    self.assertEqual(fizzbuzz(-1), None)
  def test_fizzbuzz3(self):
    self.assertEqual(fizzbuzz(3), "Fizz")
  def test_fizzbuzz5(self):
    self.assertEqual(fizzbuzz(5), "Buzz")
  def test_fizzbuzz15(self):
    self.assertEqual(fizzbuzz(15), "FizzBuzz")
if __name__ == "__main__":
    unittest.main()