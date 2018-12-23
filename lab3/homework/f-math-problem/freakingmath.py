from random import *

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(0, 30)
    y = randint(1, 30)
    
    if x >= y :
        if x % y == 0:
            op = choice(["+", "-", "*", "/"])
        else:
            op = choice(["+", "-", "*"])
    else:
        op = choice(["+", "*"])
    
    error = randint(-1, 1)

    if op == "+":
        result = x + y + error
    elif op == "-":
        result = x - y + error
    elif op == "*":
        result = x * y + error
    else:
        result = x / y + error

    return(x, y, op, result)

def check_answer(x, y, op, result, user_choice):
    if op == "+":
        if user_choice == True:
            if result == x + y:
                print("Hura")
            else:
                print("Wrong")
        else:
            if result == x + y:
                print("Wrong")
            else:
                print("Hura")
    elif op == "*":
        if user_choice == True:
            if result == x * y:
                print("Hura")
            else:
                print("Wrong")
        else:
            if result == x * y:
                print("Wrong")
            else:
                print("Hura")
    elif op == "-":
        if user_choice == True:
            if result == x - y:
                print("Hura")
            else:
                print("Wrong")
        else:
            if result == x - y:
                print("Wrong")
            else:
                print("Hura")
    else:
        if user_choice == True:
            if result == x / y:
                print("Hura")
            else:
                print("Wrong")
        else:
            if result == x / y:
                print("Wrong")
            else:
                print("Hura")