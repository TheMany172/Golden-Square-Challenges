class Spotify():
    def __init__(self):
        self.music_library = []

    def add(self, song):
        if song not in self.music_library:
            self.music_library.append(song)
        else:
            raise Exception("This song already exists")
        
    def return_all(self):
        return self.music_library