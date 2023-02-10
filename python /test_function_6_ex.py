import pytest

from function_6_ex import sum_of_list_even_numbers

@pytest.mark.parametrize("numbers, expected", [
    [[3, 6, 8], 14],
    [[1, 3, 5], 0]
    ])
def test_sum_of_list_even_numbers(numbers: list, expected: int):
    
    result = sum_of_list_even_numbers(numbers)
    assert result == expected