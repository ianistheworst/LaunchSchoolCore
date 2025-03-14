import json

"""
Mr. Calculator- A Simple program to calculate and return
the operation of two values
"""


with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

LANGUAGE = 'el'

def prompt(message):
    print(f'==> {message}')

def invalid_number(string):
    try:
        float(num1)
    except ValueError:
        return True
    return False

def messages(message, lang='en'):
    return MESSAGES[lang][message]


prompt(messages('welcome', 'el'))

prompt('What is the first number?')
num1 = input()
while invalid_number(num1):
    prompt(messages('invalid_number'))
    num1 = input()

prompt('What is the second number?')
num2 = input()
while invalid_number(num2):
    prompt('Invalid entry, please enter a valid float')
    num2 = input()

prompt("""What operation would you like to perform 
==> 1) Add 2) Subtract 3) Multiply 4) Divide""")

operation = input()

while operation not in ['1', '2', '3', '4']:
    prompt('invalid entry, please choose a valid operation option')
    operation = input()

match operation:
    case '1':
        output = float(num1) + float(num2)
    case '2':
        output = float(num1) - float(num2)
    case '3':
        output = float(num1) * float(num2)
    case '4':
        output = float(num1) / float(num2)


prompt(f'The result is {output}')