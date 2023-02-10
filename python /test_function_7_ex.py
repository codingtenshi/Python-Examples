import pytest

from function_7_ex import add_odd_numbers_in_list

@pytest.mark.parametrize("numbers, expected",[
    [[2, 3, 5, 6, -7], 1],
    [[2, 4, 6, 8], 0],
])
def test_add_odd_numbers_in_list(numbers, expected):
    result = add_odd_numbers_in_list(numbers)
    assert result == expected
   
def test_add_odd_numbers_in_list_with_string():
     numbers = [1, 3, 5, "5"]
     with pytest.raises(TypeError):
        add_odd_numbers_in_list(numbers)