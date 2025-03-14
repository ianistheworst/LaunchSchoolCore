def lines(question):
    print('-' * 72)
    print(f'Question {question}\n')


lines(1)
numbers = [1, 2, 3, 4]
#numbers.clear() #method one
print(numbers)
while numbers:
    del numbers[-1]
print(numbers)

lines(2)

#Q2
print([1, 2, 3] + [4, 5]) #got it wrong, remember it combines lists

lines(3)

#Q3
str1 = "hello there"
str2 = str1
str2 = "goodbye!"
print(str1) #I believe it will output 'hello there'--I was correct

lines(4)

#Q4
my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)#I think it will output the original list. the copy method will make a separate copy in memory of the list, i think.
#I was wrong. It makes a shallow copy so the changes are applied to the original list

lines(5)

#Q5
def is_color_valid(color):
    valid_colors = ['blue', 'green']
    #return color == 'blue' or color == 'green'
    return color in ['blue', 'green']
    #return color in valid_colors
print(is_color_valid('green'))
print(is_color_valid('blue'))
print(is_color_valid('red'))
