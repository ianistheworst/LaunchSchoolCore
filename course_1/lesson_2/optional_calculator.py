def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False
while True:

    prompt('Welcome to Calculator!')

    prompt("What's the first number?")
    number1 = input()

    while invalid_number(number1):
        prompt("Hmm... that doesn't look like a valid number.")
        number1 = input()

    prompt("What's the second number?")
    number2 = input()

    while invalid_number(number2):
        prompt("Hmm... that doesn't look like a valid number.")
        number2 = input()

    prompt("What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide")
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt("You must choose 1, 2, 3, or 4")
        operation = input()

    match operation:
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            output = float(number1) / float(number2)

    prompt(f"The result is {output:.2f}")
    cont = input('Would you like to perform more calculations? (Y/N)')
    while True:
        if cont == 'y'.casefold():
            break
        elif cont == 'n'.casefold():
            print('Have a great day!')
            quit()
        else:
            print('not a valid reply! Continue calculating? (y/n)')
            cont = input()