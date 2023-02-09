import pytest

from calculator import add_numbers,substrac_numbers,divide_numbers

def test_add_numbers():
    # given
    a = 10
    b = 5
    # when
    result = add_numbers(a, b)
    # then 
    assert result == 15

def test_add_numbers2(): # drugi sposób
    a = 10
    b = 5
    assert add_numbers(a, b) == 15

def test_add_numbers_with_negtive_values():
    a = -10
    b = 5
    result = add_numbers(a, b)
    assert result == -5

"""
assert result < 3
assert result is None
assert not result
assert result is True
"""

@pytest.mark.parametrize("a, b, expected", [
    [5, 1, 4],
    [-5, 1, -6],
    [-5, -1, -4],
    [0, -1, 1]
],
ids = ["positive values", "negative values", "test3", "test4"])
def test_substract_numbers(a: int, b: int, expected: int):
    result = substrac_numbers(a, b)
    assert result == expected
    
@pytest.mark.parametrize("a, b, expected",[
    [6, 2, 3],
    [10, 4, 2.5]
])        
def test_divide_numbers(a: int, b: int, expected: int):
    result = divide_numbers(a, b)
    assert result == expected
    
def test_divide_by_zero():
    a = 10
    b = 0
    with pytest.raises(ZeroDivisionError):
        divide_numbers(a, b)