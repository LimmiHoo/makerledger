# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: MakerLedger
import json, os, sys

def bulk_delete_entries(data_file, entry_type, confirm=False):
    """Bulk delete entries of a given type from the ledger data file."""
    if not confirm:
        print(f"⚠️  Bulk delete {entry_type} entries requires confirmation. Set confirm=True to proceed.")
        return False

    with open(data_file, 'r') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = {}

    if entry_type not in data:
        print(f"❌ Entry type '{entry_type}' not found in ledger.")
        return False

    original_count = len(data[entry_type])
    deleted = 0
    remaining = []

    for i, item in enumerate(data[entry_type]):
        if 'id' in item and item['id'] == str(i + 1):
            print(f"🗑️  Deleted {entry_type} #{i+1}")
            deleted += 1
        else:
            remaining.append(item)

    data[entry_type] = remaining
    with open(data_file, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"✅ Bulk delete complete. Removed {deleted}/{original_count} {entry_type} entries.")
    return True

if __name__ == "__main__":
    data_path = "maker_ledger_data.json"
    if len(sys.argv) > 1:
        entry_type = sys.argv[1]
    else:
        print("Usage: python bulk_delete.py <entry_type>")
        sys.exit(1)

    confirm = input("Type 'y' to confirm bulk delete, anything else to cancel: ").strip().lower() == 'y'
    if not confirm:
        print("Cancelled.")
