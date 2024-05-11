def do_add(a, b):
    return a+b


def do_sub(a, b):
    return a-b


def do_div(a, b):
    try:
        return a/b
    except ZeroDivisionError as e:
        return "Cannot divide by Zero"
    
