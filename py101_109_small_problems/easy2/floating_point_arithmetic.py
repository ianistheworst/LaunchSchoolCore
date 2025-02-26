def arithmetic():
    num1 = float(input('==> Enter the first number\n'))
    num2 = float(input('==> Enter the second number \n'))

    print(f'{num1} + {num2} = {num1 + num2}')
    print(f'{num1} - {num2} = {(num1 - num2):.2f}')
    print(f'{num1} * {num2} = {num1 * num2}')
    print(f'{num1} / {num2} = {num1 / num2}')
    print(f'{num1} // {num2} = {num1 // num2}')
    print(f'{num1} % {num2} = {num1 % num2}')
    print(f'{num1} ** {num2} = {num1 ** num2}')

arithmetic()
