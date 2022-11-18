from lib.todo_list import *

def test_incomplete_return():
    Todolist = TodoList()
    assert Todolist.incomplete() == []

def test_complete_return():
    Todolist = TodoList()
    assert Todolist.complete() == []

#Write test for nothing to give up