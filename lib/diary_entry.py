import datetime
class DiaryEntry():
    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        self.entry = f"{title}: {contents}"
        self.title = title
        self.contents = contents
        self.lis = []
        self.used_list = []
    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        list = []
        if self.entry == '':
            return 0
        else:
            x = self.entry.split(' ')
            for i in x:
                if i !=  '': ## Prevent blank spaces from being included in word count
                    list.append(i)
            return len(list)
    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        minutes_to_read_text = round((self.count_words()/ wpm), 2)
        time = str(datetime.timedelta(minutes = minutes_to_read_text))
        return time
    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        time_to_read_text = self.reading_time(wpm)
        number_of_words_i_have_time_for = wpm * minutes
        if self.used_list == [] and self.lis == []:
            x = self.entry.split(' ')
            for i in x:
                if i !=  '': ## Prevent blank spaces from being included in word count
                    self.lis.append(i)
            if self.lis != []:
                current_chunck = " ".join(self.lis[0: number_of_words_i_have_time_for])
                self.used_list += self.lis[:number_of_words_i_have_time_for]
                self.lis = self.lis[(number_of_words_i_have_time_for):]
                return current_chunck
            else:
                self.lis.append(self.used_list)
                self.used_list.clear()
        else:
            if self.lis != []:
                current_chunck = " ".join(self.lis[0: number_of_words_i_have_time_for])
                self.used_list += self.lis[:number_of_words_i_have_time_for]
                self.lis = self.lis[(number_of_words_i_have_time_for):]
                return current_chunck
            else:
                self.lis += self.used_list
                self.used_list.clear()
                current_chunck = " ".join(self.lis[0: number_of_words_i_have_time_for])
                self.used_list += self.lis[:number_of_words_i_have_time_for]
                self.lis = self.lis[(number_of_words_i_have_time_for):]
                return current_chunck
