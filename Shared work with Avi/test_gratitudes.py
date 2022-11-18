from lib.gratitudes import *

def test_add():
    gratidue = Gratitudes()
    gratidue.add("Avi")
    assert gratidue.format() == "Be grateful for: Avi"


def test_multiple_add():
    gratitude = Gratitudes()
    gratitude.add("Ibrahim")
    gratitude.add("Avi")
    assert gratitude.format() == "Be grateful for: Ibrahim, Avi"

def test_empty_add():
    gratitude = Gratitudes()
    gratitude.add("")
    assert gratitude.format() == "Be grateful for: "