# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: MakerLedger
class LedgerReport:
    """Compute summary stats across all recorded builds."""

    def __init__(self, ledger):
        self.ledger = ledger

    @staticmethod
    def _safe_int(value):
        return int(float(value)) if value is not None else 0

    def total_material_cost(self):
        return sum(self._safe_int(m.cost) for m in self.ledger.materials())

    def total_task_time_seconds(self):
        return sum(self._safe_int(t.duration_seconds) for t in self.ledger.tasks())

    def average_experiment_cycles(self):
        cycles = [self._safe_int(e.cycles_run) for e in self.ledger.experiments()]
        if not cycles:
            return 0
        return sum(cycles) / len(cycles)

    def total_budget_spent(self):
        return self.total_material_cost() + self.average_experiment_cycles() * 5

    def summary_report(self):
        m = self.ledger.materials()
        t = self.ledger.tasks()
        e = self.ledger.experiments()
        return {
            "materials_count": len(m),
            "total_material_cost": self.total_material_cost(),
            "task_count": len(t),
            "total_task_time_seconds": self.total_task_time_seconds(),
            "experiment_count": len(e),
            "average_experiment_cycles": self.average_experiment_cycles(),
            "budget_spent": self.total_budget_spent(),
        }

    def to_csv(self, filename):
        rows = [self.summary_report()]
        with open(filename, "w") as f:
            keys = list(rows[0].keys())
            header = ",".join(keys) + "\n"
            for row in rows:
                line = ",".join(str(row.get(k, "")) for k in keys) + "\n"
                f.write(line)

    def print_summary(self):
        s = self.summary_report()
        print("=== MakerLedger Summary ===")
        for k, v in s.items():
            print(f"{k}: {v}")
