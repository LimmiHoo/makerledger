# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: MakerLedger
def validate_ledger(db):
    warnings, errors = [], []
    for mat in db.materials:
        if mat.stock < 0:
            errors.append(f"Material {mat.name}: negative stock {mat.stock}")
        elif mat.stock == 0 and not any(t for t in db.tasks if t.action == 'replenish' and t.material_id == mat.id):
            warnings.append(f"Material {mat.name}: out of stock")
    for task in db.tasks:
        if task.cost < 0:
            errors.append(f"Task {task.title or task.id}: negative cost {task.cost}")
        elif task.duration and task.duration < 0:
            errors.append(f"Task '{task.title or task.id}': negative duration")
    for exp in db.experiments:
        if not (exp.temperature is None) == (exp.temp_unit is None):
            errors.append(f"Experiment {exp.id}: inconsistent temperature/unit")
    total_cost = sum(t.cost for t in db.tasks if hasattr(t, 'cost')) + sum(m.price * m.stock for m in db.materials if hasattr(m, 'price') and hasattr(m, 'stock'))
    if total_cost < 0:
        errors.append("Ledger shows negative total cost")
    return warnings, errors
