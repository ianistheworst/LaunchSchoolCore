from datetime import datetime as dt

def retire():
    age = int(input("What is your current age?"))
    retirement = int(input("What age would you like to retire"))
    now = dt.now().year
    print(f"It's {now}. You will retire in {retirement - age + now}.")
    print("Just kidding, you will never retire. USA! USA!")
    print(f"Only the rest of your life (or {retirement - age} years to go!)")

retire()