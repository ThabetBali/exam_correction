from src.rating import rate_note

def test_rate_9_returns_unsuccessful():
    assert rate_note(9) == "unsuccessful"

def test_rate_10_returns_acceptable():
    assert rate_note(10) == "acceptable"

def test_rate_8_returns_unsuccessful():
    assert rate_note(8) == "unsuccessful"