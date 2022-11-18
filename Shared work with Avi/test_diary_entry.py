from lib.diary_entry import *

def test_format():
    diary_entry = DiaryEntry("Day 1", "These are the contents.")
    assert diary_entry.format() == "Day 1: These are the contents."
    

def test_count_words_contents():
    diary_entry = DiaryEntry("Day 1", "These      are the contents.")
    assert diary_entry.count_words() == 6

def test_reading_time():
    diaryentry = DiaryEntry("Day 1", "These are the contents very odd number of words in this sentence so it gives us a weird answer")
    assert ":04:12" in diaryentry.reading_time(5)

def test_reading_chunk():
    diaryentry = DiaryEntry("Day 1", "These are the contents very odd number of words in this sentence so it gives us a weird answer")
    assert diaryentry.reading_chunk(2, 10) == "Day 1: These are the contents very odd number of words in this sentence so it gives us a weird"

def test_long_reading_chunk(): ### 96 words
    diaryentry= DiaryEntry("Day 1", """The best monologues stick to you regardless of whether you relate to what they’re saying or not. It could be the portrayal of the actor or actress, or maybe the way the tears choked them up. Famous monologues have become timeless. The best drama movies often have your favorite movie monologues, with lessons humanity can never forget. It could be an angry monologue filled with purpose and conviction, or sometimes even a dramatic monologue that can twist a knife inside your heart. It’s possible that you came looking for monologues to feel these things.""")
    diaryentry.reading_chunk(2, 10)
    diaryentry.reading_chunk(2, 10)
    diaryentry.reading_chunk(2, 10)
    diaryentry.reading_chunk(2, 10)
    
    assert diaryentry.reading_chunk(2, 10) == "knife inside your heart. It’s possible that you came looking for monologues to feel these things."

def test_long_reading_loop_chunk(): ### 96 words
    diaryentry= DiaryEntry("Day 1", """The best monologues stick to you regardless of whether you relate to what they’re saying or not. It could be the portrayal of the actor or actress, or maybe the way the tears choked them up. Famous monologues have become timeless. The best drama movies often have your favorite movie monologues, with lessons humanity can never forget. It could be an angry monologue filled with purpose and conviction, or sometimes even a dramatic monologue that can twist a knife inside your heart. It’s possible that you came looking for monologues to feel these things.""")
    diaryentry.reading_chunk(2, 10)
    diaryentry.reading_chunk(2, 10)
    diaryentry.reading_chunk(2, 10)
    diaryentry.reading_chunk(2, 10)
    diaryentry.reading_chunk(2, 10)
    assert diaryentry.reading_chunk(2, 10) == "Day 1: The best monologues stick to you regardless of whether you relate to what they’re saying or not. It"


def test_long_reading_3loop_chunk(): ### 21 words
    diaryentry= DiaryEntry("Day 1", """These are the contents very odd number of words in this sentence so it gives us a weird answer.""")
    diaryentry.reading_chunk(1, 10)
    diaryentry.reading_chunk(1, 10)
    diaryentry.reading_chunk(1, 10)
    diaryentry.reading_chunk(1, 10)
    diaryentry.reading_chunk(1, 10)
    assert diaryentry.reading_chunk(1, 10) == "answer."