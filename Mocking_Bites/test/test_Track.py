from lib.Track import * 

"""
will make basic tests for this - then move to test in the other file,
but without importing this one
to learn about Mocking
"""

import pytest

# can store in it - list
def test_can_store_title_artist():
    track1 = Track('We will rock you', 'Queen')
    assert track1.track_list == ['We will rock you', 'Queen']

#test for matches 
def test_matches():
    track1 = Track('We will rock you', 'Queen')
    assert track1.matches('will') == True

def test_non_matching():
    track1 = Track('We will rock you', 'Queen')
    with pytest.raises(Exception) as error:
        track1.matches('elephant')
    error_message = str(error.value)
    assert error_message == "Sorry that is not there"


