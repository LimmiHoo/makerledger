# === Stage 20: Add duplicate detection for newly created records ===
# Project: MakerLedger
def check_duplicates(records, new_record):
    if isinstance(new_record, dict):
        return any(r.get("id") == new_record.get("id") for r in records)
    return False
