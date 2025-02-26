def greeting():
    name = input('Ay gurl what yo name?')
    if name.endswith('!'):
        print(f'HELLO {name.upper()} WHY ARE YOU SCREAMING AT ME???')
    else:
        print(f'Hello, {name}')


greeting()
greeting()