# File: lib/music_library.py

class MusicLibrary:
    # Public properties:
    #   tracks: a list of instances of Track

    def __init__(self):
        self.library_list = []

    def add(self, track):
        # track is an instance of Track
        # Track gets added to the library
        # Returns nothing
        self.library_list.append(track)

    def search(self, keyword):
        # keyword is a string
        # Returns a list of instances of track that match the keyword
        list_to_return = []
        for i in self.library_list:
            if i.matches() == True:
                list_to_return.append(i)
        return list_to_return
        