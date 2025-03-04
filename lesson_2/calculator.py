"""
Mr. Calculator- A Simple programe to calculate and return
the operation of rtwo values
"""

def prompt(message):
    print(f'==> {message}')

def invalid_number(string):
    try:
        int(num1)
    except ValueError:
        return True
    return False


prompt('Welcome to Mr. Calculator!')

prompt('What is the first number?')
num1 = input()
while invalid_number(num1):
    prompt('Invalid entry, please enter a valid number integer')
    num1 = input()

prompt('What is the second number?')
num2 = input()
while invalid_number(num2):
    prompt('Invalit entry, please enter a valid integer')
    num2 = input()

prompt("""What operation would you like to perform 
==> 1) Add 2) Subtract 3) Multiply 4) Divide""")

operation = input()

while operation not in ['1', '2', '3', '4']:
    prompt('invalid entry, please choose a valid operation option')
    operation = input()

match operation:
    case '1':
        output = int(num1) + int(num2)
    case '2':
        output = int(num1) - int(num2)
    case '3':
        output = int(num1) * int(num2)
    case '4':
        output = int(num1) / int(num2)


prompt(f'The result is {output}')