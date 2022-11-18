from lib.todo import *
import pytest
def test_create_task_instance_check_status():
    todo = Todo("Walk the dog")
    assert todo.task_status == False 

def test_create_task_instance_check_task():
    todo = Todo("Walk the dog")
    assert todo.task == "Walk the dog"

def test_create_task_instance_check_empty_task():
    with pytest.raises(Exception) as error:
        todo = Todo("")
    e = str(error.value)
    assert e == "You need to enter a task"

def test_create_task_complete_check_task():
    todo = Todo("Walk the dog")
    todo.mark_complete()
    assert todo.task_status == True