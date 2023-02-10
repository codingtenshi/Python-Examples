from datetime import datetime
from function_3_ex import what_time_is_it

def test_what_time_is_it():
    expected = datetime.now().date()
    
    result = what_time_is_it()
    assert result.date() == expected