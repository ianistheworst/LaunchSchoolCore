def centre_of(string: str):
    length = len(string)
    if string.strip() == '':
        return 'String must not be empty'
    elif length % 2 == 0:
        return (string[(length // 2) - 1] + string[length // 2])
    elif length % 2 != 0:
        return string[length // 2]
    

print(centre_of('I Love Python!!!') == "Py")    # True
print(centre_of('Launch School') == " ")        # True
print(centre_of('Launchschool') == "hs")        # True
print(centre_of('Launch') == "un")              # True
print(centre_of('Launch School is #1') == "h")  # True
print(centre_of('x') == "x")                    # True