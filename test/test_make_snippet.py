from lib.make_snippet import *
import pytest 

def test_return_string_with_less_than_five():
    assert make_snippet("str qwert") == "str qwert"

def test_empty_string():
    assert make_snippet("") == ""

def test_check_valid_argument():
    with pytest.raises(Exception) as err:
        make_snippet(True)
    error_message = str(err.value)
    assert error_message == "This is not a string!"

def test_long_string_with_ellipsis():
    assert make_snippet("This is a very very very long string!") == "This is a very very..."