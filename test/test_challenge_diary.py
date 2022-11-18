from lib.challenge_diary import *
from lib.challenge_diaryentry import *

#test to check that we can create a diary with a list - nothing added so empty 
def test_diary_exists():
    diary1 = Diary()
    assert diary1.entry_list == []

#test to check that we can create a diary with a list and add and return the item on the list
def test_make_one_entry_into_diary():
    diary1 = Diary()
    diary_entry1 = Diary_Entry('Day 1', 'talking about my day and what i did')
    diary1.add_entry(diary_entry1) #this should add the above entry
    assert diary1.entry_list == [diary_entry1]

#test to check that we can create a diary with a list and add and return multiple items
def test_make_multiple_entry_into_diary():
    diary1 = Diary()
    diary_entry1 = Diary_Entry('Day 1', 'talking about my day and what i did')
    diary1.add_entry(diary_entry1) #this should add the above entry
    diary_entry2 = Diary_Entry('Day 2', 'Another entry - the second one i have had to write')
    diary1.add_entry(diary_entry2) #this should add the above entry
    assert diary1.entry_list == [diary_entry1, diary_entry2]

#test to get block of text that can be read in given time
def test_for_entries_that_can_be_read():
    diary1 = Diary()
    diary_entry1 = Diary_Entry('Day 1', 'talking about my day and what i did')
    diary1.add_entry(diary_entry1) #this should add the above entry
    diary_entry2 = Diary_Entry('Day 2', 'Another entry the second one i have had to write')
    diary1.add_entry(diary_entry2) #this should add the above entry
    assert diary1.select_best_entry_to_read(5, 10) == [diary_entry1, diary_entry2]

#test to get block of text that one can be read and the other cannot in the given time
def test_for_entries_that_one_can_be_read_and_the_other_cannot():
    diary1 = Diary()
    diary_entry1 = Diary_Entry('Day 1', 'talking about my day and what i did')
    diary1.add_entry(diary_entry1) #this should add the above entry
    diary_entry2 = Diary_Entry('Day 2', 'Another entry the second one i have had to write, this is the longer one of the two')
    diary1.add_entry(diary_entry2) #this should add the above entry
    assert diary1.select_best_entry_to_read(2, 5) == [diary_entry1]

#test to return a list of mobile numbers in entries 
def test_for_mobile_numbers_returned():
    diary1 = Diary()

    diary_entry1 = Diary_Entry('Day 1', 'talking about my day and what i did')
    diary1.add_entry(diary_entry1) #this should add the above entry

    diary_entry2 = Diary_Entry('Day 2', 'Another entry the second one i have had to write 07936527167')
    diary1.add_entry(diary_entry2) #this should add the above entry

    diary_entry3 = Diary_Entry('Day 3', 'Working hard today, no time for slacking, number is 07536726188')
    diary1.add_entry(diary_entry3) #this should add the above entry

    assert diary1.find_mobile_phone() == ['07936527167', '07536726188']

def test_for_mobile_numbers_sometooshort_someno0():
    diary1 = Diary()
    diary_entry1 = Diary_Entry('Day 1', 'talking about my day, my number is 74521458799 and what i did')
    diary1.add_entry(diary_entry1) #this should add the above entry
    diary_entry2 = Diary_Entry('Day 2', 'Another entry the second one i have had to write 0793652716')
    diary1.add_entry(diary_entry2) #this should add the above entry
    diary_entry3 = Diary_Entry('Day 3', 'Working hard today, no time for slacking, number is 07536726188')
    diary1.add_entry(diary_entry3) #this should add the above entry
    
    assert diary1.find_mobile_phone() == ['07536726188']

def test_for_mobile_numbers_not_numbers():
    diary1 = Diary()
    diary_entry1 = Diary_Entry('Day 1', 'talking about my day, my number is 0hfyeudjgyt and what i did')
    diary1.add_entry(diary_entry1) #this should add the above entry
    diary_entry2 = Diary_Entry('Day 2', 'Another entry the second one i have had to write 0793652716')
    diary1.add_entry(diary_entry2) #this should add the above entry
    diary_entry3 = Diary_Entry('Day 3', 'Working hard today, no time for slacking, number is 07536726188')
    diary1.add_entry(diary_entry3) #this should add the above entry
    
    assert diary1.find_mobile_phone() == ['07536726188']