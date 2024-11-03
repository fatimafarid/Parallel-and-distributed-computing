<<<<<<< HEAD
def calculator():
    operation = input("Select operation (+, -, *, /): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operation == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operation == '*':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operation == '/':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation!")

if __name__ == "__main__":
=======
def calculator():
    operation = input("Select operation (+, -, *, /): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operation == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operation == '*':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operation == '/':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation!")

if __name__ == "__main__":
>>>>>>> 15be036 (Added chap3 to chap9 folders)
    calculator()