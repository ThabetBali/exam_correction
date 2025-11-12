import pytest

from src.rating import rate_note


@pytest.mark.parametrize("note", [7, 8, 9])
def test_rate_note_unsuccessful(note):
    assert rate_note(note) == "unsuccessful"

@pytest.mark.parametrize("note", [10, 11, 12])
def test_rate_note_acceptable(note):
    assert rate_note(note) == "acceptable"

def test_rate_note_13_good():
    assert rate_note(13) == "good"

def test_rate_note_14_good():
    assert rate_note(14) == "good"
