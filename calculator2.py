on = True
def add():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a+b)

def substraction():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a - b)

def multiply():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a * b)

def divide():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a / b)

while on:
    operation = input("Please type +, -, *, / or Q")
    if operation == '+':
        add()
    elif operation == '-':
        substraction()
    elif operation == '*':
        multiply()
    elif operation == '/':
        divide()
    elif operation == 'q':
        calc_on = False
    else:
        print("That operation is not available. ")
