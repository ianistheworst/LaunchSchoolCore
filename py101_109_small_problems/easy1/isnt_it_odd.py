def isnt_it_odd(num):
    if abs(num) % 2 == 0:
        return True
    else:
        return False

#Official Solution- clearly more efficient
# def is_odd(number):
#     return abs(number) % 2 == 1
    
print(isnt_it_odd(4))
print(isnt_it_odd(5))
print(isnt_it_odd(-4))
print(isnt_it_odd(-5))