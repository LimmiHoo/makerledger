# === Stage 4: Implement create operations for the primary records ===
# Project: MakerLedger
def create_record(record_type, **kwargs):
    """Create a primary record (material, task, cost, experiment, snapshot) with validation."""
    records = {
        "material": {"id": kwargs["name"], "type": kwargs.get("type", "raw"), "quantity": float(kwargs.get("qty", 0)), "unit_cost": float(kwargs.get("cost_per_unit", 0)), "notes": kwargs.get("notes", "")},
        "task": {"id": kwargs["title"], "description": kwargs.get("desc", ""), "duration_minutes": int(kwargs.get("hours", 0)) * 60, "assigned_to": kwargs.get("assigned", ""), "status": kwargs.get("status", "pending")},
        "cost": {"item_id": kwargs.get("material_name"), "quantity_used": float(kwargs.get("qty_used", 0)), "unit_cost": float(kwargs.get("price_per_unit", 0)), "total": round(float(kwargs.get("qty_used", 0)) * float(kwargs.get("price_per_unit", 0)), 2), "date": kwargs.get("date", ""), "notes": kwargs.get("notes", "")},
        "experiment": {"title": kwargs["name"], "hypothesis": kwargs.get("hypothesis", ""), "methodology": kwargs.get("methodology", ""), "observations": kwargs.get("observations", ""), "conclusion": kwargs.get("conclusion", ""), "materials_used": []},
        "snapshot": {"project_name": kwargs.get("project", ""), "date": kwargs.get("date", ""), "description": kwargs.get("desc", ""), "progress_pct": float(kwargs.get("progress", 0)), "current_materials": [], "current_costs": [], "notes": kwargs.get("notes", "")}
    }

    if record_type not in records:
        raise ValueError(f"Unknown record type: {record_type}. Use material, task, cost, experiment, or snapshot.")

    base = records[record_type]
    for key, val in kwargs.items():
        if key == "id":
            continue  # skip ID auto-generation
        if hasattr(base, key):
            setattr(base, key, val)

    return base
