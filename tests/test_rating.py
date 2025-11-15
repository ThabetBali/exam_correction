import pytest

from src.rating import rate_note


@pytest.mark.parametrize("note,expected", [(0, "unsuccessful"), (1, "unsuccessful"), (2, "unsuccessful"),
                                           (3, "unsuccessful"), (4, "unsuccessful"), (5, "unsuccessful"),
                                           (6, "unsuccessful"), (7, "unsuccessful"), (8, "unsuccessful"),
                                           (9, "unsuccessful"), (10, "acceptable"), (11, "acceptable"),
                                           (12, "acceptable"), (13, "good"), (14, "good"), (15, "very good"),
                                           (16, "very good"), (17, "excellent"), (18, "excellent"),
                                           (19, "excellent"), (20, "excellent")])
def test_rate_note(note, expected):
    assert rate_note(note) == expected

@pytest.mark.parametrize("note,expected", [(-1, "Impossible note value. Value must be between 0 and 20."),
                                           (21, "Impossible note value. Value must be between 0 and 20.")])
def test_rate_returns_Impossible(note, expected):
    with pytest.raises(
        ValueError, match=expected
    ):
        rate_note(note)
