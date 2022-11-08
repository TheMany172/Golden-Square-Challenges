from lib.count_words import *
import pytest


def test_check_valid_argument():
    with pytest.raises(Exception) as err:
        count_words(True)
    error_message = str(err.value)
    assert error_message == "This is not a string!"

def test_for_empty_str():
    assert count_words("") == 0

def test_for_1_word():
    assert count_words("whatever") == 1

def test_for_multiple_word():
    assert count_words("whatever i don't care") == 4