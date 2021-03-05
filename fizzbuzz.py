def fizzbuzz(num):
  if num < 0 or num > 100:
    return None
  if num % 3 == 0:
    return "Fizz"
  return num