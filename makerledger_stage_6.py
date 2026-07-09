# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: MakerLedger
def delete_entry(record, confirm=False):
    """Remove a record from the ledger by ID with an optional confirmation flag."""
    if record["id"] in ledger:
        if not confirm and input("Delete this entry? [y/N] ") != "y":
            return False
        del ledger[record["id"]]
        print(f"Entry {record['id']} deleted.")
        return True
    else:
        print(f"No entry with ID {record.get('id')} found.")
        return False
