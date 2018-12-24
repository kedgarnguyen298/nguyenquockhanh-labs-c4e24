def evaluate(x, y, op):
    if op == "+":
        result = x + y    
    elif op == "-":
        result = x - y
    elif op == "*":
        result = x * y
    else:
        result = x / y

    return(result)
