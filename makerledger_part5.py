# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: MakerLedger
class Ledger:
    def __init__(self):
        self._records = {}

    def update_material(self, name, qty=0, cost=None, note=""):
        if name in self._records:
            rec = self._records[name]
            rec["qty"] += qty
            if cost is not None and rec.get("cost") is None:
                rec["cost"] = cost * rec["qty"]
            rec["note"] = note
            return rec
        else:
            raise KeyError(f"Material '{name}' not found in ledger")

    def update_task(self, name, status="done", duration=0):
        if name in self._records:
            rec = self._records[name]
            rec["status"] = status
            rec["duration"] += duration
            return rec
        else:
            raise KeyError(f"Task '{name}' not found in ledger")

    def update_cost(self, category, amount=0):
        if category in self._records:
            rec = self._records[category]
            rec["amount"] += amount
            return rec
        else:
            raise KeyError(f"Cost category '{category}' not found in ledger")

    def add_experiment(self, name, result="unknown"):
        key = f"exp_{name}"
        if key not in self._records:
            self._records[key] = {"name": name, "result": result}
            return self._records[key]
        else:
            rec = self._records[key]
            rec["result"] = result
            return rec

    def snapshot(self):
        return dict(sorted(self._records.items()))
