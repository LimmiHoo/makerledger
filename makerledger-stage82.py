# === Stage 82: Add an end-to-end demo function that prints a complete walkthrough ===
# Project: MakerLedger
import json
from dataclasses import asdict

def demo():
    m = {"name": "wood", "quantity": 2, "unit_price": 5.0}
    t = {"task": "cut to size", "duration_hours": 3}
    e = {"experiment": "glue test", "success": True}
    s = {"project": "bench_v1", "date": "2024-06-01"}

    ledger = {
        "materials": [m],
        "tasks": [t],
        "experiments": [e],
        "snapshots": [s]
    }
    total_cost = m["quantity"] * m["unit_price"] + t["duration_hours"] * 10.0

    print(f"Project: {s['project']}")
    print(f"Materials used: {m['name']} x {m['quantity']} @ ${m['unit_price']:.2f}")
    print(f"Task: {t['task']} (${(t['duration_hours']*10):.2f})")
    print(f"Experiment: {e['experiment']} -> {'success' if e['success'] else 'failed'}")
    print(f"Total cost: ${total_cost:.2f}")

    with open("ledger.json", "w") as f:
        json.dump(ledger, f, indent=2)
    print("\nLedger saved to ledger.json")
