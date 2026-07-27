# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: MakerLedger
def reset_demo_data(db, logger):
    """Clear all demo data and re-populate with a small fresh set."""
    for table in [
        "projects", "materials", "tasks", "costs",
        "experiments", "project_snapshots"
    ]:
        db.execute(f"DELETE FROM {table}")

    logger.info("Demo data cleared.")

    projects = [
        {"name": "Wooden Bench",  "owner": "alice",   "start": "2024-11-01"},
        {"name": "Metal Shelf",    "owner": "bob",     "start": "2024-11-05"},
        {"name": "Paper Prototype","owner": "charlie","start": "2024-11-10"},
    ]

    materials = [
        ("plywood",       8.5,   "m3"),
        ("steel_angle",   12.0,  "kg"),
        ("cardboard",     0.5,   "sheets"),
    ]

    tasks = [
        {"project": "Wooden Bench",  "name": "Cut plywood"},
        {"project": "Metal Shelf",    "name": "Bend steel angles"},
        {"project": "Paper Prototype","name": "Sketch layout"},
    ]

    costs = [
        {"task": "Cut plywood",      "item": "plywood",   "qty": 1, "price": 8.50},
        {"task": "Bend steel angles","item": "steel_angle","qty": 2,"price": 6.00},
    ]

    experiments = [
        {"project": "Wooden Bench","note": "Tested joint strength"},
    ]

    snapshots = [
        {"project": "Wooden Bench","date": "2024-11-03", "status": "in_progress"},
        {"project": "Metal Shelf",   "date": "2024-11-07","status": "planned"},
    ]

    db.executemany(
        "INSERT INTO projects (name, owner, start) VALUES (:n,:o,:s)",
        [(p["name"], p["owner"], p["start"]) for p in projects],
    )
    db.executemany(
        "INSERT INTO materials (name, price, unit) VALUES (:n,:p,:u)",
        [(m[0], m[1], m[2]) for m in materials],
    )
    db.executemany(
        "INSERT INTO tasks (project, name) VALUES (:pr,:nm)",
        [(t["project"], t["name"]) for t in tasks],
    )
    db.executemany(
        "INSERT INTO costs (task, item, qty, price) VALUES (:ts,:it,:q,:pr)",
        [(c["task"], c["item"], c["qty"], c["price"]) for c in costs],
    )
    db.executemany(
        "INSERT INTO experiments (project, note) VALUES (:pr,:nt)",
        [(e["project"], e["note"]) for e in experiments],
    )
    db.executemany(
        "INSERT INTO project_snapshots (project, date, status) VALUES (:pr,:dt,:st)",
        [(s["project"], s["date"], s["status"]) for s in snapshots],
    )

    logger.info("Demo data re-populated successfully.")
