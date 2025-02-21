def tip_calc():
    bill = float(input('What is the total bill?\n'))
    tip_percent = int(input('What is the tip percentage?\n'))

    tip = (tip_percent / 100) * bill
    total = bill + tip
    print(f'The tip amount is ${tip:.2f} for a {tip_percent}% tip.')
    print(f'The total is ${total:.2f}')

tip_calc()