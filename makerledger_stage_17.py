# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: MakerLedger
def dry_run(self, action: str) -> str:
    """Return a simulated outcome without mutating state."""
    records = {
        "add_material": self._material_template,
        "add_task": self._task_template,
        "add_cost": self._cost_template,
        "add_experiment": self._experiment_template,
        "snapshot": self._snapshot_template,
    }
    if action not in records:
        return f"[DRY-RUN] Unknown action '{action}'"
    template = records[action].copy()
    for key, val in self._dry_run_context.items():
        template[key] = val
    return template
