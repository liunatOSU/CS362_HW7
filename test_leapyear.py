import unittest
from leapyear import leapyear

class TestLeapYear(unittest.TestCase):
  def test_leapyear5(self):
    self.assertEqual(leapyear(5), False)
    
if __name__ == "__main__":
    unittest.main()