def to_capital_case(value):
    if not isinstance(value, str):
        raise TabError ("Please provide string")
    
    for char in value:
        if char.isdigit():
            raise TabError("Please remove numbers from the string")
    return value.capitalize()
    