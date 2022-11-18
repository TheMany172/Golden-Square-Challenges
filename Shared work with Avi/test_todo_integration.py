from lib.todo import *
from lib.todo_list import *
import pytest

def test_todo_incomplete_list_add():
    todo_list = TodoList()
    task1 = Todo("Walk the dog")
    todo_list.add(task1)
    assert todo_list.incomplete() == [task1]

def test_todo_complete_list_add():
    todo_list = TodoList()
    task1 = Todo("Walk the dog")
    task1.mark_complete()
    todo_list.add(task1)
    assert todo_list.complete() == [task1]

def test_todo_update_complete_list_add():
    todo_list = TodoList()
    task1 = Todo("Walk the dog")
    todo_list.add(task1)
    task1.mark_complete()
    assert todo_list.complete() == [task1]

def test_todo_invalid_todo_list_add():
    todo_list = TodoList()
    with pytest.raises(Exception) as error:
        task1 = Todo("")
    e = str(error.value)
    assert e == "You need to enter a task"

def test_give_up():
    todo_list = TodoList()
    task1 = Todo("Walk the dog")
    task2 = Todo("Walk the turtle")
    task3 = Todo("Walk the horsse")
    todo_list.add(task1)
    todo_list.add(task2)
    todo_list.add(task3)
    todo_list.give_up()
    assert todo_list.incomplete() == []

def test_todo_complete_give_up_list_add():
    todo_list = TodoList()
    task1 = Todo("Walk the dog")
    task1.mark_complete()
    todo_list.add(task1)
    with pytest.raises(Exception) as error:
        todo_list.give_up()
    e = str(error.value)
    assert e == "All tasks are already complete"