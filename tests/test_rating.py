import pytest

from src.rating import rate_note


@pytest.mark.parametrize("note", [7, 8, 9])
def test_rate_note_unsuccessful(note):
    assert rate_note(note) == "unsuccessful"

@pytest.mark.parametrize("note", [10, 11, 12])
def test_rate_note_acceptable(note):
    assert rate_note(note) == "acceptable"

@pytest.mark.parametrize("note", [13, 14])
def test_rate_note_good(note):
    assert rate_note(note) == "good"
