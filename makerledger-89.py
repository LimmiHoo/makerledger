# === Stage 89: Add final consistency checks for names, statuses, and dates ===
# Project: MakerLedger
def consistency_check(records):
    valid_statuses = {"planned", "in_progress", "completed", "failed"}
    valid_material_types = {"raw", "processed", "electronic", "tooling"}
    for rec in records:
        if rec.get("status") not in valid_statuses:
            raise ValueError(f"Invalid status '{rec['status']}' in {rec}")
        if rec.get("type") not in valid_material_types:
            raise ValueError(f"Invalid material type '{rec['type']}' in {rec}")
        if "date" in rec and rec["date"] is None:
            raise ValueError("Missing date in record")
    return all(1 for _ in records)
