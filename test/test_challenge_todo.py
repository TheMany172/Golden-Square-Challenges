from lib.challenge_todo import *


#test for a blank list
def test_blank_list():
    todo1 = Todo()
    todo1.add_todo_item('walk the dog')
    assert todo1.todo_list == ['walk the dog']

#test for a list with items, and return them
def test_populated_list():
    todo1 = Todo()
    todo1.add_todo_item('walk the dog')
    assert todo1.return_whole_list() == ['walk the dog']


#test for a list with items, and return them
def test_populated_list_multiple_items():
    todo1 = Todo()
    todo1.add_todo_item('walk the dog')
    todo1.add_todo_item('walk the cat')
    todo1.add_todo_item('walk the cow')
    assert todo1.return_whole_list() == ['walk the dog', 'walk the cat', 'walk the cow']