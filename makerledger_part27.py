# === Stage 27: Add monthly summary calculations ===
# Project: MakerLedger
def monthly_summary(records):
    """Summarize records by month: spend, task count, and material usage."""
    months = {}
    for r in records:
        key = (r["month"], r["year"])
        if key not in months:
            months[key] = {"spend": 0.0, "tasks": 0, "materials": {}}
        months[key]["spend"] += float(r.get("cost", 0))
        if r.get("type") == "task":
            months[key]["tasks"] += 1
        if r.get("type") == "material":
            mat = r["name"]
            months[key]["materials"][mat] = months[key]["materials"].get(mat, 0) + float(r.get("quantity", 0))
    return sorted(months.items())
