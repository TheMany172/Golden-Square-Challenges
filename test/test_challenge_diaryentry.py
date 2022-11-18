from lib.challenge_diaryentry import *
#test that diary entry exists
def test_for_diary_entry_exists():
    diary_entry = Diary_Entry('Day 1', 'today was a good day, i got work done')
    assert diary_entry.contents == 'today was a good day, i got work done'

# #test that checks the formatting of the entry
# def test_formatted():
#     diary_entry = Diary_entry('Day 1', 'today was a good day, i got work done')
#     assert diary_entry.formatted == 'Day 1: today was a good day, i got work done'

# #test that counts the words in the entry
# def test_count_words():
# diary_entry = Diary_entry('Day 1', 'today was a good day, i got work done')
# assert diary_entry.count_words() == 11