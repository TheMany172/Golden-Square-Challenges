
    As a user
    So that I can record my experiences
    I want to keep a regular diary

    As a user
    So that I can reflect on my experiences
    I want to read my past diary entries

    As a user
    So that I can reflect on my experiences in my busy day
    I want to select diary entries to read based on how much time I have and my reading speed

what is the reading speed wpm and time
know the length of the entries
be able to match the closes one - rounded up

    As a user
    So that I can keep track of my tasks
    I want to keep a todo list along with my diary

    As a user
    So that I can keep track of my contacts
    I want to see a list of all of the mobile phone numbers in all my diary entries


# plain text
- diary that can store things
- want to be able to read previous entries
- select an entry based on reading time
- 

Diary
- be able to store entries
- call back entries
- pick a diary entry based on reading time and wpm

Diary entries
- create an entry (to be added to the diary class)
- know the length/time needed for an entry
- find mobile numbers in text


Todo items
- adding and storing items
- recalling those items


## Shells of the methods and classes

# Diary class
class Diary():
    __init__(self):
    self.entry_list = []
    
No needed arguments - will want a list or something to store the entries

def add_entry(self):
- should take an instance of diaryentry
- should add entry to diary 
- returns nothing
- side effects are that it adds the entry to the list in diary


def diary_entries(self):
-takes none
- should return all of our diary entries - as a list

def select_best_entry_to_read(self, wpm, time):
- this takes time and wpm as int (with time being minutes, and wpm as wpm)
- should return the diary entry that could be read in the given amount of time, 
taking into account the reading speed


def find_mobile_numbers():
- takes nothing
- should return a list - of the numbers - in all entries

# DiaryEntry class
class Diary_Entry():
    __init__(self, title, contents)
    self.title
    self.contents

    def joining(title,): 


# todo class
class Todo():
      __init__(self, task):
      self.task_list = []
      
    def add():
- take 1 string
- this should add todo items to the list
- return nothing

    def todo_list():
- this should call back the list of todo items
- take no arguments
- return a list of all items


--------------

# example tests

#test to check that we can create a diary with a list - nothing added so empty 
def test_diary_exists():
diary1 = Dairy()
assert diary1.entry_list == []

#test to check that we can create a diary with a list and add and return the item on the list
def test_make_one_entry_into_diary():
diary1 = Dairy()
diary_entry1 = Diary_Entry('Day 1', 'talking about my day and what i did')
diary1.add(diary_entry1) #this should add the above entry
assert diary1.entry_list == ['Day 1: talking about my day and what i did']

#test to check that we can create a diary with a list and add and return multiple items
def test_make_multiple_entry_into_diary():
diary1 = Dairy()
diary_entry1 = Diary_Entry('Day 1', 'talking about my day and what i did')
diary1.add(diary_entry1) #this should add the above entry
diary_entry2 = Diary_Entry('Day 2', 'Another entry - the second one i have had to write')
diary1.add(diary_entry2) #this should add the above entry
assert diary1.entry_list == ['Day 1: talking about my day and what i did','Day 2: Another entry - the second one i have had to write']

#test to get block of text that can be read in given time
def test_for_entries_that_can_be_read
diary1 = Dairy()
diary_entry1 = Diary_Entry('Day 1', 'talking about my day and what i did')
diary1.add(diary_entry1) #this should add the above entry
diary_entry2 = Diary_Entry('Day 2', 'Another entry the second one i have had to write')
diary1.add(diary_entry2) #this should add the above entry
assert diary1.select_best_entry_to_read(3, 4) == ['Day 1: talking about my day and what i did', 'Day 2: Another entry the second one i have had to write']

#test to get block of text that one can be read and the other cannot in the given time
def test_for_entries_that_one_can_be_read_and_the_other_cannot
diary1 = Dairy()
diary_entry1 = Diary_Entry('Day 1', 'talking about my day and what i did')
diary1.add(diary_entry1) #this should add the above entry
diary_entry2 = Diary_Entry('Day 2', 'Another entry the second one i have had to write')
diary1.add(diary_entry2) #this should add the above entry
assert diary1.select_best_entry_to_read(3, 3) == ['Day 1: talking about my day and what i did']

#test to return a list of mobile numbers in entries 
def test_for_mobile_numbers_returned
diary1 = Dairy()
diary_entry1 = Diary_Entry('Day 1', 'talking about my day and what i did')
diary1.add(diary_entry1) #this should add the above entry
diary_entry2 = Diary_Entry('Day 2', 'Another entry the second one i have had to write 07936527167')
diary1.add(diary_entry2) #this should add the above entry
diary_entry3 = Diary_Entry('Day 3', 'Working hard today, no time for slacking, number is 07536726188')
diary1.add(diary_entry2) #this should add the above entry
assert diary1.find_mobile_phone() == ['07936527167', '07536726188']

#test that diary entry exists
def test_for_diary_entry_exists
diary_entry = Diary_entry('Day 1', 'today was a good day, i got work done')
assert diary_entry == 'Day 1', 'today was a good day, i got work done'

#test that checks the formatting of the entry
def test_formatted()
diary_entry = Diary_entry('Day 1', 'today was a good day, i got work done')
assert diary_entry.formatted == 'Day 1: today was a good day, i got work done'

#test that counts the words in the entry
def test_count_words():
diary_entry = Diary_entry('Day 1', 'today was a good day, i got work done')
assert diary_entry.count_words() == 11

# Todo tests
class Todo():
    __init__(self)
    self.todo_list = []

def test_add_todo_item(self, string1):
    self.todo_list.append(string1)

def return_whole_list():
    return self.todo_list

#test for a blank list
def test_blank_list():
    todo1 = Todo()
    assert todo1.todo_list == []

#test for a list with items, and return them
def test_populated_list():
    todo1 = Todo()
    todo1.add_todo_item('walk the dog')
    todo1.add_todo_item('walk the cat')
    todo1.add_todo_item('walk the cow')
    assert todo1.return_whole_list == ['walk the dog', 'walk the cat', 'walk the cow']













