integer = int(input('Please enter an integer greater than 0:\n'))
s_or_p = input('Please enter "s" to compute sum or "p" to compute product\n')

if s_or_p == 's':
    print(sum(range(1, integer+1)))
    #My original inefficient solution
    # total = 0
    # for i in range(1, (integer + 1)):
    #     total += i
    #     #print(total)
    # print(f'The sum is {total}')

elif s_or_p == 'p':
    total = 1
    for i in range(1, (integer + 1)):
        total *= i
        print(total)
    print(f'The product of all numbers is {total}')
