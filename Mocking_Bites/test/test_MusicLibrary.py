from lib.MusicLibrary import * 

""" 
Having done unit test for track

now will try to do full integration test in this one but only using fake class/mocking

test init?

test add with fake instance of track or a mocking track

keyword also
"""
from unittest.mock import Mock

def test_add_with_mock():
    musiclibrary1 = MusicLibrary()

    fake_track_entry = Mock()
    fake_track_entry.return_value = ['Breakthru, Queen']

    fake_track_entry1 = Mock()
    fake_track_entry1.return_value = ['coming down, FFDP']

    musiclibrary1.add(fake_track_entry)
    musiclibrary1.add(fake_track_entry1)
    assert musiclibrary1.library_list == [fake_track_entry, fake_track_entry1]

def test_search_with_mock():
    musiclibrary1 = MusicLibrary()

    fake_track_entry = Mock()
    fake_track_entry.return_value = ['Breakthru, Queen']
    fake_track_entry.matches.return_value = False


    fake_track_entry1 = Mock()
    fake_track_entry1.return_value = ['coming down', 'FFDP']
    fake_track_entry1.matches.return_value = True

    fake_track_entry2 = Mock()
    fake_track_entry2.return_value = ['down by the river', 'Porcupine Tree']
    fake_track_entry2.matches.return_value = True

    musiclibrary1.add(fake_track_entry)
    musiclibrary1.add(fake_track_entry1)
    musiclibrary1.add(fake_track_entry2)

    assert musiclibrary1.search('down') == [fake_track_entry1, fake_track_entry2]