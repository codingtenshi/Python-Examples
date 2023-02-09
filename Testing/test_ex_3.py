import pytest

from ex_3 import to_capital_case

def test_format_to_capital_case():
    value = "python"
    
    assert to_capital_case(value) == "Python"
    
def test_raises_exception_if_value_not_string():
    value = 12
    
    with pytest.raises(TabError):
        to_capital_case(value)
        
def test_raises_exceptions_if_string_contains_numbers():
    value = "ma2"
    
    with pytest.raises(TabError):
        to_capital_case(value)
    
    
