# === Stage 11: Add JSON export for the current application state ===
# Project: MakerLedger
def export_json(self):
    state = {
        "materials": [m.as_dict() for m in self.materials],
        "tasks": [t.as_dict() for t in self.tasks],
        "costs": [c.as_dict() for c in self.costs],
        "experiments": [e.as_dict() for e in self.experiments],
        "snapshots": [s.as_dict() for s in self.snapshots],
    }
    return json.dumps(state, indent=2)
