def negative(num: int):
    return -abs(num)
    # if num <= 0:
    #     return num
    # else:
    #     return (num * -1)
    
print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True  