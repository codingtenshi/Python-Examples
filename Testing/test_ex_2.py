from ex_2 import sum_args

def test_sum_args_below_max_value():
    max_value = 12
    elements = [1, 5, 3, 10]
    expected = 19
    
    result = sum_args (max_value, *elements)
    assert result == expected
    
def test_sum_args_above_max_value():
    max_value =  12
    elements = [1, 2, 40,10]
    
    result = sum_args(max_value, *elements)
    assert result == 13
    
def test_sum_args_with_element_equal_max_value():
    max_value = 12
    elements= [ 1, 2, 12, 13]
    
    result = sum_args(max_value, *elements)
    assert result == 15
    
def test_sum_args_with_mixed_type():
    max_value =  12
    elements = [ 1, 5, 'kot', 3, 10, None]
    
    result = sum_args(max_value, *elements)
    assert result == 19
    
def test_sum_args_with_max_value_string():
    max_value = "invalid"
    elements = [1, 2, 3, 4]
    
    result = sum_args(max_value, *elements)
    assert result == 10
    
def test_sum_args_with_no_elements():
    max_value =  12
    elements = []
    
    result = sum_args(max_value, *elements)
    assert result == 0   
    
 
    
    