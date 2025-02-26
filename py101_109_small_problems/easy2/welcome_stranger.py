# def greetings(list, dict):
#     return f"""hello {list[0]} {list[1]} {list[2]}! Nice to have a {dict['title']} {dict['occupation']} around"""

def greetings(list, dict):
    return(f"Hello, {' '.join(list)}! Great to have a {dict['title']} "
           f"{dict['occupation']} around!")
greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.