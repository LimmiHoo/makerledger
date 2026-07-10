# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: MakerLedger
def sort_entries(entries, field="date"):
    if field == "title":
        return sorted(entries, key=lambda e: (e.get("priority", 0), e["title"]))
    elif field == "priority":
        return sorted(entries, key=lambda e: (e.get("priority", 0) or 0, -int(e.get("date") or 0)))
    elif field == "last_update":
        return sorted(entries, key=lambda e: e["last_update"], reverse=True)
    else:
        return sorted(entries, key=lambda e: e[field], reverse=True)

def add_sorting_to_ledger(ledger):
    ledger["sort_fields"] = {
        "title": lambda e: (e.get("priority", 0), e["title"]),
        "date": lambda e: -int(e.get("date") or 0),
        "priority": lambda e: e.get("priority", 0) or 0,
        "last_update": lambda e: e["last_update"],
    }
    return ledger

def get_sorted_entries(ledger, field="date"):
    if not ledger["sort_fields"]:
        return ledger["entries"][:]
    key = ledger["sort_fields"][field]
    return sorted(ledger["entries"], key=key)
