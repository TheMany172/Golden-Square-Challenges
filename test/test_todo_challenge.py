from lib.todo_challenge import *

def test_todo_is_present():
    assert todo_check("This is my to do list #TODO: get milk from the store.") == True

def test_todo_not_present():
    assert todo_check("This is my to do list get milk from the store.") == False