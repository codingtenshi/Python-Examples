def add_numbers(a: int, b: int):
    return a + b

def substrac_numbers(a: int, b: int):
    return a - b

def divide_numbers(a: int, b: int) -> float:
    if b == 0:
        raise ZeroDivisionError("You cannot divide by zero")
    return a/b