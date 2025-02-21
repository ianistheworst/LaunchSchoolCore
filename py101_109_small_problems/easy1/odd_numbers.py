for i in range(1, 100, 2):
    print(i)

#Further Exploration
def odd_numbers(start, end):
    if start % 2 == 0:
        for i in range(start + 1, end, 2):
            print(i)
    else:
        for i in range(start, end, 2):
            print(i)

odd_numbers(1, 10)
odd_numbers(2, 10)
odd_numbers(2, 11)
odd_numbers(17, 50)