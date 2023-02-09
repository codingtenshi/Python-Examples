"""
function needs returne sum of transferred arguments, 
if argument is not bigger than max_value
"""

def sum_args(max_value, *args):
    sum_elements = 0
    
    max_value = max_value if isinstance(max_value, int) else 100:
    
    for value in args:
        if isinstance(value, int) and value <= max_value:
            sum_elements += value
            
    return sum_elements