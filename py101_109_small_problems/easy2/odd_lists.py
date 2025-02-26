def oddities(arg):
    arg_list = []
    num = 1
    while num < len(arg):
        arg_list.append(arg[num])
        num += 2
    print(arg_list)
    return arg[::2]



    return arg_list

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True
