# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: MakerLedger
import json, os

class LedgerDemo:
    def __init__(self):
        self.projects = {}
        self.materials = {
            "wood": {"cost": 2.50, "unit": "kg"},
            "nails": {"cost": 0.15, "unit": "box"},
            "glue": {"cost": 0.80, "unit": "bottle"}
        }
        self.tasks = {}
        self.experiments = {}

    def add_material(self, name, quantity):
        cost = self.materials[name]["cost"] * quantity
        record = {name: quantity}
        self.tasks[f"buy_{name}_{quantity}"] = {"action": "purchase", "record": record, "total_cost": cost}
        return cost

    def add_task(self, name, description):
        self.tasks[name] = {"description": description}

    def log_experiment(self, name, result):
        self.experiments[name] = {"result": result}

    def save_snapshot(self):
        snapshot = {
            "materials_purchased": sum(t["total_cost"] for t in self.tasks.values() if t["action"] == "purchase"),
            "tasks_done": len([t for t in self.tasks.values()]),
            "experiments_done": len(self.experiments)
        }
        return snapshot

demo = LedgerDemo()
demo.add_material("wood", 5)
demo.add_task("assemble_frame", "Build wooden frame")
demo.log_experiment("test_glue_strength", "passed")
snapshot = demo.save_snapshot()
print(json.dumps(snapshot, indent=2))
