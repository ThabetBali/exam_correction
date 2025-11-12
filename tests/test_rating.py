from src.rating import rate_note


def test_rate_note_is_callable():
    rate_note(9)

def test_rate_9_returns_unsuccessful():
    assert rate_note(9) == "unsuccessful"