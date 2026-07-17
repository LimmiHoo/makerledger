# === Stage 28: Add overdue item detection based on due dates ===
# Project: MakerLedger
def find_overdue_items(leader, project):
    """Return a list of (item_id, item) for items past their due date."""
    today = datetime.date.today()
    overdue = []
    for item in project.items:
        if hasattr(item, 'due_date') and item.due_date:
            try:
                if item.due_date < today:
                    overdue.append((item.id, item))
            except TypeError:
                pass
    return overdue

def mark_overdue_items(project):
    """Mark each overdue item with a status flag for quick identification."""
    today = datetime.date.today()
    for item in project.items:
        if hasattr(item, 'due_date') and item.due_date and item.due_date < today:
            setattr(item, 'is_overdue', True)
