from lib.Todo import *

"""
Basic Plan -
this one appears to be for taking in tasks and assigning complete or the default - incomplete

TEST EXAMPLES:

# can i store something?
todo1 = Todo('Walk the dog') #initalize
assert todo1.variablename == 'Walk the dog'

#can i store and then mark something as complete?
todo1 = Todo('Walk the dog') 
todo1.mark_complete()
assert todo1.variablename == 'Walk the dog' - True

"""
def test_init_then_recal_task():
    todo = Todo('Walk the cat')
    assert todo.todo_list == {'Walk the cat' : False}

def test__multiple_init_then_recal_tasks():
    todo = Todo('Walk the cat')
    todo2 = Todo('Do a food shop')
    assert todo.todo_list == {'Walk the cat' : False} and todo2.todo_list == {'Do a food shop' : False}

def test_mark_complete():
    todo = Todo('Walk the cat')
    todo.mark_complete()
    assert todo.todo_list == {'Walk the cat' : True}