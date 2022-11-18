from lib.grammarstats import *

def test_check():
    grammarstats = GrammarStats()
    assert grammarstats.check("Hello, how are you?") == True

def test_percentage_good_nothing_entered():
    grammarstats = GrammarStats()
    assert grammarstats.percentage_good() == "you've not checked anything - moron."

def test_percentage_good_one_entry():
    grammarstats = GrammarStats()
    grammarstats.check("Hello, how are you?")
    assert grammarstats.percentage_good() == 100

def test_percentage_good_multi_entry():
    grammarstats = GrammarStats()
    grammarstats.check("Hello, how are you?")
    grammarstats.check("Hello, how are you?")
    grammarstats.check("ello, how are you?")
    grammarstats.check("Hello, how are you")
    assert grammarstats.percentage_good() == 50

