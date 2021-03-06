def fizzbuzz(num):
  if num < 0 or num > 100:
    return None
  if num % 3 == 0 and num % 5 == 0:
    return "FizzBuzz"
  if num % 3 == 0:
    return "Fizz"
  if num % 5 == 0:
    return "Buzz"
  return num