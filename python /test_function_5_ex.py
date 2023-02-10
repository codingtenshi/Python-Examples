import pytest

from function_5_ex import sum_of_list_numbers

def test_sum_of_list_numbers():
    numbers = [-4, 9,-6]
    expected = -1
    
    result = sum_of_list_numbers(numbers)
    assert result == expected
    
def test_raises_exception_sum_of_list_numbers_with_string():
    numbers = "m"
    with pytest.raises(TypeError):
        sum_of_list_numbers(numbers)
        

    
 

    

    
    