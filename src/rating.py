def rate_note(note):
    if note < 10:
        return "unsuccessful"
    if 10 <= note < 13:
        return "acceptable"
    if note == 15:
        return "very good"
    return "good"
