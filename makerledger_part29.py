# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: MakerLedger
def reminders(items, days_ahead=7):
    """Return items due within `days_ahead` days from today."""
    import datetime
    now = datetime.date.today()
    cutoff = now + datetime.timedelta(days=days_ahead)
    return [i for i in items if i.get('due_date', None) and i['due_date'] <= cutoff]
