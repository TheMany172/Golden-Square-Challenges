'''
    As a user
    So that I can keep track of my tasks
    I want a program that I can add todo tasks to and see a list of them.

    As a user
    So that I can focus on tasks to complete
    I want to mark tasks as complete and have them disappear from the list.

- be able to store tasks
- return all tasks
- be able to 'mark complete' which removes them from the list

Class todo_tracker

- init - (nothing to be taken here)

- function 'add' - takes '1 string'
    - adds the string as a todo item to a list (or whatever we store it as)
    
- function 'return_all' - takes nothing
    - returns all remaining items that are not completed - that have previously been added

- function 'mark_complete' - takes one string (a todo list item)
    - checks if the string is in the list of items and then removes it

'''

from lib.todo_tracker import *
import pytest

def test_return_all():
    todo = Todo_Tracker()
    assert todo.return_all() == []

def test_1_task():
    todo = Todo_Tracker()
    todo.add('walk the cat')
    assert todo.return_all() == ["walk the cat"]

def test_3_tasks():
    todo = Todo_Tracker()
    todo.add('walk the cat')
    todo.add('walk the horse')
    todo.add('walk the hippo')
    assert todo.return_all() == ["walk the cat", "walk the horse", "walk the hippo"]

def test_3_tasks_then_remove_1():
    todo = Todo_Tracker()
    todo.add('walk the cat')
    todo.add('walk the horse')
    todo.add('walk the hippo')
    todo.mark_complete('walk the horse')
    assert todo.return_all() == ["walk the cat", "walk the hippo"]

def test_3_tasks_then_failed_remove():
    todo = Todo_Tracker()
    todo.add('walk the cat')
    todo.add('walk the horse')
    todo.add('walk the hippo')
    with pytest.raises(Exception) as error:
        todo.mark_complete('walk the house')
    error_message = str(error.value)
    assert error_message == "This task does not exist :-("
