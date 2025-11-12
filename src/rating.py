def rate_note(note):
    if note < 10:
        return "unsuccessful"
    if 10 <= note < 13:
        return "acceptable"
    if 13 <= note < 15:
        return "good"
    if 15 <= note < 17:
        return "very good"
    return "excellent"
