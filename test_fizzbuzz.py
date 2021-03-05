import unittest
from fizzbuzz import fizzbuzz

class TestFizzbuzz(unittest.TestCase):
  def test_fizzBuzzInvalid(self):
    self.assertEqual(fizzbuzz(-1), None)
  
if __name__ == "__main__":
    unittest.main()