# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: MakerLedger
def filter_entries(entries, **kwargs):
    """Filter ledger entries by status, category, owner, tag, or date range."""
    result = []
    for entry in entries:
        if kwargs.get("status") and entry.status != kwargs["status"]:
            continue
        if kwargs.get("category") and entry.category != kwargs["category"]:
            continue
        if kwargs.get("owner") and entry.owner != kwargs["owner"]:
            continue
        if kwargs.get("tags"):
            if not any(t in kwargs["tags"] for t in entry.tags):
                continue
        if "min_date" in kwargs:
            try:
                if entry.date < kwargs["min_date"]:
                    continue
            except TypeError:
                pass
        if "max_date" in kwargs:
            try:
                if entry.date > kwargs["max_date"]:
                    continue
            except TypeError:
                pass
        result.append(entry)
    return result
