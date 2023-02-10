import pytest

from function_8_ex import return_sum_of_int_in_char

@pytest.mark.parametrize("sentence, expected", [
    ["Bl5a, bla7git status, bla", 2],
    ["223hga552", 6]
])

def test_return_sum_of_int_in_char(sentence, expected):
    result = return_sum_of_int_in_char(sentence)
    assert result == expected