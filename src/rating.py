def rate_note(note):
    if note < 10:
        return "unsuccessful"
    if note == 13:
        return "good"
    return "acceptable"
