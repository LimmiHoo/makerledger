# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: MakerLedger
def format_cost_row(item_name: str, qty: float, unit_price: float) -> str:
    """Return a formatted ledger row string for a material cost entry."""
    total = qty * unit_price
    return f"{item_name:<25s}  {qty:>10.2f} x ${unit_price:>8.2f} = ${total:>10.2f}"


def format_task_row(task_id: str, description: str, status: str) -> str:
    """Return a formatted ledger row string for a task entry."""
    return f"{task_id:<6s} | {description:<40s} | [{status}]"


def summarize_costs(materials: list[dict], tasks: list[dict]) -> dict[str, float]:
    """Compute total material and labor costs from raw records.

    Parameters
        materials: list of dicts with 'qty' (float) and 'unit_price' (float).
        tasks:     list of dicts with 'hours' (float) and 'hourly_rate' (float).

    Returns a dict with keys 'material_total', 'labor_total', 'grand_total'.
    """
    material_total = sum(m['qty'] * m['unit_price'] for m in materials if isinstance(m.get('qty'), (int, float)) and isinstance(m.get('unit_price'), (int, float)))
    labor_total = sum(t['hours'] * t['hourly_rate'] for t in tasks if isinstance(t.get('hours'), (int, float)) and isinstance(t.get('hourly_rate'), (int, float)))
    return {
        'material_total': material_total,
        'labor_total': labor_total,
        'grand_total': material_total + labor_total,
    }
