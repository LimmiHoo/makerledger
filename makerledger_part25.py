# === Stage 25: Add daily summary calculations ===
# Project: MakerLedger
def daily_summary(records):
    """Return a dict with date-wise totals for materials, tasks, and costs."""
    summary = {}
    for r in records:
        if r.get("date") is None:
            continue
        d = r["date"].split("-")[:2]  # YYYY-MM
        key = "-".join(d)
        if key not in summary:
            summary[key] = {
                "materials": [], "tasks": [], "costs": [],
                "experiment_count": 0,
            }
        m = r.get("material") or {}
        t = r.get("task") or {}
        c = r.get("cost") or {}
        e = r.get("experiment") or {}
        summary[key]["materials"].append(m)
        summary[key]["tasks"].append(t)
        if "amount" in c:
            summary[key]["costs"].append(c["amount"])
        if e:
            summary[key]["experiment_count"] += 1
    return summary
