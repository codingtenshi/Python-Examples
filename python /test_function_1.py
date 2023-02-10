import pytest

from function_1_ex import string_starts_with_a

@pytest.mark.parametrize("word, expected", [
    ["mummy", False],
    ["apple", True],
    ["Apple", True]
])
def test_string_starts_with_not_a_or_A_char1(word: str, expected: bool):
    
    result = string_starts_with_a(word)
    assert result == expected