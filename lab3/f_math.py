from random import randint, choice
from calc import evaluate

#1. Generate equation
x = randint(0, 9)
y = randint(0, 9)
error = randint(-1, 1)
oper = choice(["+", "-", "*", "/"])
r = evaluate(x, y, oper) + error

print(f"{x} {oper} {y} = {r}")

while True:
    user_answer = input("Y/N? ").upper()
    
    if user_answer == "Y":
        if error == 0:
            print("Yay")
            break
        else:
            print("Wrong!")
            break
    elif user_answer == "N":
        if error == 0:
            print("Wrong!")
            break
        else:
            print("Yayy")
            break
    else:
        print("Y or N?")
