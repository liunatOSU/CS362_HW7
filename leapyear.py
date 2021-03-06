def leapyear(year):
  if year % 4 != 0:
    return False
  if year % 100 != 0:
    return True
  return False 