num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
choice = input("Enter +, -, *, /: ")

if choice == "+":
  print(num1 + num2)
elif choice == "-":
  print(num1 - num2)
elif choice == "*":
  print(num1 * num2)
elif choice == "/":
  if num2 == 0:
    print("Cannot be divided by zero")
  else:
    print(num1 / num2)
else:
  print("Wrong input")