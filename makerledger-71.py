# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: MakerLedger
def seed_demo_data():
    """Generate deterministic sample data for MakerLedger."""
    import hashlib, random
    rng = random.Random(42)

    materials = [
        {"name": "LED strip", "qty": 5, "unit_price": 8.99},
        {"name": "Arduino Uno", "qty": 3, "unit_price": 19.99},
        {"name": "Resistor pack", "qty": 20, "unit_price": 3.49},
        {"name": "Breadboard", "qty": 5, "unit_price": 6.79},
    ]

    tasks = [
        {"title": "Wire LED matrix", "duration_hours": 3},
        {"title": "Install drivers", "duration_hours": 1},
        {"title": "Write control script", "duration_hours": 4},
        {"title": "Test integration", "duration_hours": 2},
    ]

    costs = [
        {"category": "hardware", "amount": 150.75},
        {"category": "software", "amount": 0.00},
        {"category": "shipping", "amount": 12.99},
    ]

    experiments = []
    for i in range(3):
        exp_id = hashlib.md5(f"exp-{i}".encode()).hexdigest()[:8]
        experiments.append({
            "id": exp_id,
            "name": f"Wobble test {i+1}",
            "notes": f"Observed oscillation at 22Hz. Tuned damping to reduce amplitude.",
            "success": rng.choice([True, False]),
        })

    snapshots = []
    for day in range(5):
        total_cost = sum(c["amount"] for c in costs) + rng.randint(10, 30) * 5.99
        completed_tasks = [t for t in tasks if t["title"] not in ("Test integration",)]
        snapshots.append({
            "date": f"2024-11-{day+8:02d}",
            "total_spent": round(total_cost, 2),
            "completed_tasks": len(completed_tasks),
            "remaining_materials": sum(m["qty"] for m in materials) - day * 3,
        })

    return {"materials": materials, "tasks": tasks, "costs": costs,
            "experiments": experiments, "snapshots": snapshots}
