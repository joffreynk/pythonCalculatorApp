def addition(num1, num2):
  return  round(num1 + num2, 2)
def division(num1, num2):
  return round(num1 / num2, 2)

def multiplication(num1, num2):
  return  round(num1 * num2, 2)

def substraction(num1, num2):
  return  round(num1 - num2, 2)

def operations():
  print('''
  Select operation:
  1. Add.
  2.Sustract.
  3. Multiply.
  4. Divide
  5. Close The App
  ''')

while True:
  operations()
  operation = input("Enter operation: ")
  if operation == '5':
    print("""
Thank you for using our App
Bye
      """)
    break

  if operation not in ('1', '2', '3', '4', '5'):
    print("OOOOps, your operation is not valid, please Select 1, 2, 3, 4, and 5")
    continue
  while True:
    try:
      num1 = float(input("Enter the first number: "))
      break
    except ValueError:
      print("ooops,  please enter a valid number")
      continue

  while True:
    try:
      num2 = float(input("Enter the second value: "))
      break
    except ValueError:
      print("ooops, please enter a valid number")
      continue

  match operation:
    case '1':
      print(num1, " + ", num2, " = ", addition(num1, num2))
    case '2':
      print(num1, " - ", num2, " = ", substraction(num1, num2))
    case '3':
      print(num1, " * ", num2, " = ", multiplication(num1, num2))
    case '4':
      print(num1, " / ", num2, " = ", division(num1, num2))
    case _:
      print("ooops, you have selected wrong operation, please Redo")
      continue
