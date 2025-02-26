def penultimate(string: str):
    words = string.split(' ')
    if len(words) > 1:
        return words[-2]
    else:
        return 'Not enough words in string!'

# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")
print(penultimate('Ahoy!'))