import pytest
from function_4_ex import count_letter_a_in_sentence

@pytest.mark.parametrize("word, expected", [
    ["Ala ma kota", 4],
    ["apple", 1],
    ["Apple", 1]
])

def test_count_letter_a_in_sentecne(word, expected):
   
   
  
    result = count_letter_a_in_sentence(word)
    assert result == expected
