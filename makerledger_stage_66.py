# === Stage 66: Add export of a short status dashboard ===
# Project: MakerLedger
def dashboard(ledger):
    """Export a short status dashboard."""
    rows = []
    for item in ledger:
        if isinstance(item, Materials):
            total_cents = sum(m.cents for m in item)
            rows.append(f"Materials: {total_cents/100:.2f} USD")
        elif isinstance(item, Tasks):
            done = sum(1 for t in item if t.done)
            rows.append(f"Tasks: {done}/{len(item)} complete")
        elif isinstance(item, Costs):
            total = sum(c.cents for c in item)
            rows.append(f"Costs: {total/100:.2f} USD")
        elif isinstance(item, Experiments):
            success = sum(1 for e in item if e.success)
            rows.append(f"Experiments: {success}/{len(item)} succeeded")
        elif isinstance(item, Snapshots):
            snapshot = item
            rows.append(f"Snapshot at {snapshot.date}: {len(snapshot.items)} entries")
    return "\n".join(rows)
