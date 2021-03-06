import unittest
from leapyear import leapyear

class TestLeapYear(unittest.TestCase):
  def test_leapyear5(self):
    self.assertEqual(leapyear(5), False)
  def test_leapyear4(self):
    self.assertEqual(leapyear(4), True)
  def test_leapyear100(self):
    self.assertEqual(leapyear(100), False)
  def test_leapyear400(self):
    self.assertEqual(leapyear(400), True)
    
if __name__ == "__main__":
    unittest.main()