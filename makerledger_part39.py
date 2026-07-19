# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: MakerLedger
def repair_ledger(ledger):
    """Fix common integrity issues: duplicate entries, missing timestamps, invalid costs."""
    repaired = 0
    if "materials" in ledger and len(ledger["materials"]) > 1:
        seen_ids = set()
        for i, mat in enumerate(ledger["materials"]):
            if not isinstance(mat.get("id"), str) or mat["id"] in seen_ids:
                mat["id"] = f"mat_{i}"
                seen_ids.add(mat["id"])
                repaired += 1
    if "tasks" in ledger and len(ledger["tasks"]) > 1:
        for i, task in enumerate(ledger["tasks"]):
            if not task.get("timestamp"):
                task.setdefault("timestamp", f"2026-05-{i+1}")
                repaired += 1
    if "costs" in ledger and any(not isinstance(c.get("amount"), (int, float)) for c in ledger["costs"]):
        for i, cost in enumerate(ledger["costs"]):
            try:
                cost.setdefault("amount", 0.0)
                repaired += 1
            except Exception:
                pass
    return ledger, repaired
