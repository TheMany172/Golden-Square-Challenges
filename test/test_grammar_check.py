from lib.grammar_check import *


def test_check_first_character():
    assert check_first_character("How are you") == True

def test_check_punctuation_mark():
    assert check_punctuation_mark("how are you?") == True

def test_check_first_character_fail():
    assert check_first_character("how are you?") == False

def test_check_punctuation_mark_fail():
    assert check_punctuation_mark("How are you") == False

def test_grammar_check_good_grammar():
    assert grammar_check("Hello how are you?") == "Well done you have used correct punctuation and grammar!"

def test_grammar_check_bad_punctuation():
    assert grammar_check("Hello how are you") == "Sorry, you missed the punctuation mark."

def test_grammar_check_bad_grammar():
    assert grammar_check("hello how are you?") == "Sorry, you missed the capital letter."

def test_grammar_check_both_fail():
    assert grammar_check("hello how are you") == "duz yoo evans grammair%"