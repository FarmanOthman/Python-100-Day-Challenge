print("PY caculator")

first_number = int(input("First number: "))
second_number = int(input("Second number: "))

operation = input("What do you want to do? \n1. Add\n2. Substract\n3. Multiply\n4. Divide\n")

def calc(first_number, second_number, operation):
  if operation == "1":
    return first_number + second_number
  elif operation == "2":
    return first_number - second_number
  elif operation == "3":
    return first_number * second_number
  elif operation == "4":
    return first_number / second_number
  else:
    return "Invalid choice"

result = calc(first_number, second_number, operation)
print(f"The result is {result}")