# File: lib/track.py

class Track:
    def __init__(self, title, artist):
        # title and artist are both strings
        self.track_list = [title, artist]

    def matches(self, keyword):
        # keyword is a string
        # Returns true if the keyword matches either the title or artist
        for i in self.track_list:
            if keyword in i:
                return True
            else:
                raise Exception("Sorry that is not there")