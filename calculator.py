def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: can't divide by zero!"
    return a / b


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose an option:")
print("1 - Sum")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

op = input("Enter option: ")

if op == "1":
    print("Result:", sum(num1, num2))

elif op == "2":
    print("Result:", sub(num1, num2))

elif op == "3":
    print("Result:", multiplication(num1, num2))

elif op == "4":
    print("Result:", division(num1, num2))

else:
    print("Invalid operation!")