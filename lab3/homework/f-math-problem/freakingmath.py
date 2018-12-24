from random import *
from calc_func import evaluate
def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(0, 30)
    y = randint(1, 30)

    error = randint(-1, 1)
    
    if x >= y :
        if x % y == 0:
            op = choice(["+", "-", "*", "/"])
        else:
            op = choice(["+", "-", "*"])
    else:
        op = choice(["+", "*"])
    
    result = evaluate(x, y, op) + error
    
    return(x, y, op, result)

def check_answer(x, y, op, result, user_choice):
    if user_choice == True:
        if evaluate(x, y, op) == result:
            return(True)
        else:
            return(False)
    elif user_choice == False:
        if evaluate(x, y, op) == result:
            return(False)
        else:
            return(True)


    