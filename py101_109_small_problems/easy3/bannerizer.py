def print_in_box(string):
    print('+' + ('-' * (len(string) + 2)) + '+')
    print('| ' + (' ' * len(string)) + ' |')
    print('| ' + string + ' |')
    print('| ' + (' ' * len(string)) + ' |')
    print('+' + ('-' * (len(string) + 2)) + '+')

print_in_box('ahoy')
print_in_box('living life like a volcano and this is only the beginning')
print_in_box(' ')