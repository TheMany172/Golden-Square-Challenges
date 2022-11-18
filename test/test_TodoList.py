from lib.Todo import *
from lib.TodoList import *
"""
Basic Plan - 
init has nothing

add - moves an instance of the Todo class into this class and adds it to a list

incomplete - returns list of instances that have the assigned values - False

complete - returns list of instances that have the assigned values - True

give_up - changes the state of all the todos to - True

TEST EXAMPLES:

# incomplete starts as returning blank list?
todolist1 = TodoList()
todolist1.incomplete == []

# same for complete?
todolist1 = TodoList()
todolist1.complete == []

#INTEGRATED TESTS=====================================================================

#add a todo to the todolist class
todo1 = Todo('Walk the dog')
todolist1 = TodoList()
todolist1.add(todo)
assert todolist1.variable == that object item

#add and call an incomplete item
todo1 = Todo('Walk the dog')
todolist1 = TodoList()
todolist1.add(todo)
assert todolist1.incomplete() == that object item

#add and call a completed item
todo1 = Todo('Walk the dog')
todolist1 = TodoList()

todolist1.add(todo)
assert todolist1.incomplete() == that object item

"""

def test_init_list_blank():
    todolist1 = TodoList()
    assert todolist1.list_of_todos == []

# def test_init_complete_also_blank():
#     todolist1 = TodoList()
#     assert todolist1.complete == []

#add a todo to the todolist class
def test_add_todo():
    todo1 = Todo('Walk the dog')
    todolist1 = TodoList()
    todolist1.add(todo1)
    assert todolist1.list_of_todos == [todo1]

def test_add_and_return_incomplete_todo():
    todo1 = Todo('Walk the dog')
    todolist1 = TodoList()
    todolist1.add(todo1)
    assert todolist1.incomplete() == [todo1]

def test_add_and_return_multiple_incomplete_todo():
    todo1 = Todo('Walk the dog')
    todo2 = Todo('Walk the cat')
    todo3 = Todo('Walk the cow')
    todolist1 = TodoList()
    todolist1.add(todo1)
    todolist1.add(todo2)
    todolist1.add(todo3)
    assert todolist1.incomplete() == [todo1, todo2, todo3]

#add and call a completed item

def test_add_and_return_multiple_completed():
    todo1 = Todo('Walk the fish')
    todo2 = Todo('Walk the parrot')
    todo3 = Todo('Walk the monkey')
    todolist1 = TodoList()
    todo1.mark_complete()
    todo2.mark_complete()
    todo3.mark_complete()
    todolist1.add(todo1)
    todolist1.add(todo2)
    todolist1.add(todo3)
    assert todolist1.complete() == [todo1, todo2, todo3]



def test_1_complete():
    todo1 = Todo('Walk the fish')
    todo2 = Todo('Walk the parrot')
    todo3 = Todo('Walk the monkey')
    todolist1 = TodoList()
    todo1.mark_complete()
    todolist1.add(todo1)
    todolist1.add(todo2)
    todolist1.add(todo3)
    assert todolist1.complete() == [todo1]

def test_1_incomplete():
    todo1 = Todo('Walk the fish')
    todo2 = Todo('Walk the parrot')
    todo3 = Todo('Walk the monkey')
    todolist1 = TodoList()
    todo1.mark_complete()
    todo3.mark_complete()
    todolist1.add(todo1)
    todolist1.add(todo2)
    todolist1.add(todo3)
    assert todolist1.incomplete() == [todo2]


# test give up - changing all todos as complete
def test_give_up():
    todo1 = Todo('Walk the fish')
    todo2 = Todo('Walk the parrot')
    todo3 = Todo('Walk the monkey')
    todolist1 = TodoList()
    todo1.mark_complete()
    todolist1.add(todo1)
    todolist1.add(todo2)
    todolist1.add(todo3)
    # only 1 here will be complete as above, the function should make all incomplete
    todolist1.give_up()
    #then asserting to check they are complete
    assert todolist1.complete() == [todo1, todo2, todo3]