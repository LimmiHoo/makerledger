# === Stage 40: Add plain text report export ===
# Project: MakerLedger
def export_report(self, path):
    """Export a compact plain-text report of the project to *path*."""
    lines = []
    lines.append(f"Project: {self.project_name}")
    lines.append(f"Created:   {self.created_at}")
    if self.updated_at:
        lines.append(f"Updated:   {self.updated_at}")
    for m in sorted(self.materials.values(), key=lambda x: x.cost):
        qty = int(m.quantity) if isinstance(m.quantity, float) else m.quantity
        lines.append(f"{m.name} ({qty}) - ${float(m.price):.2f}/unit")
    total_cost = sum(float(m.price * (int(m.quantity) if isinstance(m.quantity, float) else m.quantity)) for m in self.materials.values())
    lines.append(f"Total cost: ${total_cost:.2f}")
    for t in sorted(self.tasks.values(), key=lambda x: x.id):
        status = "Done" if t.done else "Pending"
        lines.append(f"[{status}] {t.name} - {t.duration}m")
    for e in self.experiments:
        lines.append(f"- {e}")
    if self.snapshot:
        snap = self.snapshot
        lines.append(f"Last snapshot ({snap.date}): {len(snap.observations)} observations, {len(snap.notes)} notes")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
