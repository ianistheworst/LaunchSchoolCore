
def lines(question):
    print('-' * 72)
    print(f'Question {question}')

lines(1)

def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())