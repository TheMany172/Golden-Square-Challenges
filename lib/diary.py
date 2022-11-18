from lib.diary_entry import *
from math import ceil
class Diary():
    def __init__(self):
        self.entries = []

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        self.entries.append(entry)

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self.entries 

    def count_words_all(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        count = 0
        for diary_entry_object in self.entries:
            print (self.entries)
            count += diary_entry_object.count_words()
        return count


    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        minutes_to_read_text = ceil((self.count_words_all()/ wpm))
        return minutes_to_read_text

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        words_have_time_to_read = wpm * minutes
        closest_to_words = ""
        closest_number = 0
        for diary_entry_object in self.entries:
            current_count = diary_entry_object.count_words()
            if current_count > closest_number and current_count <= words_have_time_to_read:
                closest_number = current_count
                closest_to_words = diary_entry_object
        return closest_to_words
