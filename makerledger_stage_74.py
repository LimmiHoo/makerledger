# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: MakerLedger
def compare_snapshots(before, after):
    """Compare two project snapshots and return a dictionary of changes."""
    if isinstance(before, dict) and isinstance(after, dict):
        all_keys = set(before.keys()) | set(after.keys())
        changes = {}
        for key in sorted(all_keys):
            val_before = before.get(key)
            val_after = after.get(key)
            if val_before != val_after:
                changes[key] = {"before": val_before, "after": val_after}
        return changes
    elif isinstance(before, list) and isinstance(after, list):
        return {key: [x for x in set(after) - set(before)] for key in before if key not in after}
    else:
        raise TypeError("Both arguments must be dicts or lists")
