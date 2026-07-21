# === Stage 45: Add restore from backup with validation ===
# Project: MakerLedger
def restore_from_backup(backup_path, validate=True):
    """Restore ledger state from a JSON backup with optional validation."""
    import json, os
    if not os.path.exists(backup_path):
        raise FileNotFoundError(f"Backup file not found: {backup_path}")
    try:
        with open(backup_path) as f:
            data = json.load(f)
    except (json.JSONDecodeError, UnicodeDecodeError):
        raise ValueError("Corrupted backup file")
    if validate:
        required_keys = {"materials", "tasks", "costs", "experiments", "snapshots"}
        for key in required_keys:
            if key not in data or not isinstance(data[key], list):
                raise ValueError(f"Missing or invalid key '{key}'")
    return data
