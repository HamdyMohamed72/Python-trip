# let''s create a function for the simple mathematical operations which are : addition , subtraction , multiplication and division.
def subtraction(num1, num2):
    """function for subtracting two numbers entered by the user"""
    x = float(num1 - num2)
    return x


def addition(num1, num2):
    """function for adding two numbers entered by the user"""
    x = float(num1 + num2)
    return x


def multiplication(num1, num2):
    """function for multiplying two numbers entered by the user"""
    x = float(num1 * num2)
    return x


def division(num1, num2):
    """function for dividing two numbers entered by the user while the next if condition is to make sure that the
    second number is not a zero"""
    if num2 == 0:
        return "undefined"
    else:
        x = float(num1 / num2)
        return x


num_1 = float(input("insert your first number : "))
num_2 = float(input("insert your second number : "))

operation = int(input('''operations you can perform
1. Addition
2. Subtraction
3. Multiplication
4. Division

Your operation is number : '''))

if operation == 1:
    print(num_1, " + ", num_2, " = ",
          addition(num_1, num_2))

elif operation == 2:
    print(num_1, " - ", num_2, " = ",
          subtraction(num_1, num_2))

elif operation == 3:
    print(num_1, " * ", num_2, " = ",
          multiplication(num_1, num_2))

elif operation == 4:
    print(num_1, " / ", num_2, " = ",
          division(num_1, num_2))
else:
    print("Invalid input")
