def stringy(n):
    binary = ""
    for item in range(n):
        digit = '1' if item % 2 == 0 else '0'
        binary += digit
    # binary = []

    # while len(binary) < n:
    #     if len(binary) < n:
    #         binary.append('1')
    #     if len(binary) < n:    
    #         binary.append('0')
    # binary = ''.join(binary)

    return binary

print(stringy(5))
print(stringy(6))
print(stringy(1))
