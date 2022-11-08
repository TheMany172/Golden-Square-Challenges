from lib.estimated_reading_time import *

def test_divide_by():
    x = divide_by(500)
    assert x == 2.5

def test_get_len():
    x = get_len("returns a string that shows an estimated time to read")
    assert x == 10

def test_estimated_time():
    assert estimated_time("returns a string that shows an estimated time to read") == 0.05

def test_estimated_reading_time():
    assert estimated_reading_time("returns a string that shows an estimated time to read") == "This will take you approximately 0.05 minutes to read."