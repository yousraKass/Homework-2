from error import DivisionByZero

def division(a, b):
  if b == 0:
    raise DivisionByZero("Attemp to divide by zero")
  else:
    return a / b

