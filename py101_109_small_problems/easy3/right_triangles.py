def triangle(n):
    for i in range(n+1):
        print((' ' * (n - i)) + '*' * i)

triangle(5)