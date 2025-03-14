"""
Mrs. Loan Calculator!
This is a simple loan calculator to take some basic information
and return the monthly payment one time.
"""
import locale
locale.setlocale(locale.LC_ALL, 'C')

def format_currency(amount):
    return '${:,.2f}'.format(amount)
def invalid_loan(amount):
    try:
        number = float(amount)
        if number <= 0:
            raise ValueError(f'Value must be greater than 0: {amount}')
    except ValueError:
        return True
    return False
def invalid_apr(amount):
    try:
        number = float(amount)
        if number < 0:
            raise ValueError(f'Value must be greater than 0: {amount}')
    except ValueError:
        return True
    return False

while True:

    loan = input("What is your loan amount?\n")
    while invalid_loan(loan):
        print(f'Invalid entry, must enter a valid number (you entered {loan})')
        loan = input("What is your loan amount?\n")
    loan = float(loan)


    apr_percent = input("What is the APR %?\n")
    while invalid_apr(apr_percent):
        print(f'invalid entry. try again.')
        apr_percent = input()
    
    apr_decimal = float(apr_percent) / 100



    duration_in_months = int(input("What is the loan duration in months?\n"))

    if apr_decimal == 0:
        payment = loan / duration_in_months
        print(f'Easy. Your monthly payment is {format_currency(payment)}')
    else:
        rate = apr_decimal / 12
        payment = loan * (rate / (1 - (1 + rate) ** (-duration_in_months)))
        print(f'your monthly payment is {format_currency(payment)}.')


    cont = input('Would you like to perform another calculation (Y/n)?\n')
    while True:
        if cont.casefold() == 'y':
            break
        elif cont.casefold() == 'n':
            print('Thank you for using Mrs. Calculator!')
            quit()
        else:
            cont = input('Invalid response. Continue (y/n)?')
            