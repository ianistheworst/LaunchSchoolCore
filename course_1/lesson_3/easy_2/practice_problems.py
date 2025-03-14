def lines():
    print('-' * 72)

#Q1
numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]
#method 1
num_rev = list(reversed(numbers))
print(num_rev)
#method 2
print(numbers[::-1])

lines()

#Q2
numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)
print(number1 in numbers)
print(number2 in numbers)

lines()

#Q3
print(42 in range(10, 101)) #official answer
print(10 <= 42 <= 100)#my alternate answers
print(10 <= 100 <= 100)
print(10 <= 101 <= 100)

lines()

#Q4
nums = [1, 2, 3, 4, 5]
#nums.pop(2)#my solution- returns the removed value
del nums[2] #official solution-silently deletes the value
print(nums)

lines()

#Q5
numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}
print(type(numbers))#my solution
print(type(table))
print(isinstance(numbers, list))
print(isinstance(table, list))

lines()

#Q6
title = "Flintstone Family Members"
title = title.center(40)
print(title)

lines()

#Q7
statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."
print(statement1.count('t'))
print(statement2.count('t'))

lines()

#Q8
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}
print('Spot' in ages)

lines()

#Q9
# ages['Marilyn'] = 32
# ages['Spot'] = 237 #Long, less efficient way
additional_ages = {'Marilyn': 22, 'Spot': 237}
ages.update(additional_ages)
print(ages)