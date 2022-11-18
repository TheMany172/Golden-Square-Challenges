'''As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

- class Spotify()
    - no arguments
    - probably a list in there

- function 'add' - 1 string
    - adds a string to our library of songs (probably a list)

- function 'return_all' - no arguments
    - returns all of the songs previously added (probably as a list)
'''

from lib.music_tracker import *
import pytest


def test_return_all():
    spotify = Spotify()
    assert spotify.return_all() == []

def test_add_1_song():
    spotify = Spotify()
    spotify.add("all star")
    assert spotify.music_library == ["all star"]

def test_add_3_or_4_songs():
    spotify = Spotify()
    spotify.add("all star")
    spotify.add("killer queen")
    spotify.add("breakthru")
    spotify.add("i'm so bad with song names honestly")
    assert spotify.music_library == ["all star", "killer queen", "breakthru", "i'm so bad with song names honestly"]

def test_add_songs_song_already_exists():
    spotify = Spotify()
    spotify.add("all star")
    spotify.add("killer queen")
    spotify.add("breakthru")
    with pytest.raises(Exception) as error:
        spotify.add("breakthru")
    error_message = str(error.value)
    assert error_message == "This song already exists"
    