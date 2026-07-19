# === Stage 37: Add recommendations for the next useful action ===
# Project: MakerLedger
def suggest_next_action(self, recent_entries: list[dict], context_window: int = 5) -> str:
    """Generate a concise recommendation for the next useful action based on recent activity."""
    if len(recent_entries) == 0:
        return "Begin by adding your first material to the workshop ledger."

    last_entry = recent_entries[-1]
    entry_type = last_entry.get("type", "")
    
    # If we just added a material, suggest logging a task or cost
    if entry_type == "material":
        total_cost = sum(e.get("cost") or 0 for e in recent_entries if e.get("type") == "material" and isinstance(e.get("cost"), (int, float)))
        if total_cost > 50:
            return f"With ${total_cost:.1f} spent on materials, consider logging a cost entry to track expenses."
        else:
            return "You've added a material. Consider adding a task that uses this material next."

    # If we just added a task or cost, suggest an experiment or snapshot
    if entry_type in ("task", "cost"):
        return "Consider running an experiment with your current setup and take a project snapshot afterward."

    # General fallback based on last action type
    action_map = {
        "material": "Add a task that uses this material.",
        "task": "Log the cost of resources consumed in this task.",
        "cost": "Run an experiment to test your current setup, then take a snapshot.",
        "experiment": "Take a project snapshot to capture progress so far.",
        "snapshot": "Review recent entries and plan your next material or task purchase."
    }
    return action_map.get(entry_type, "Continue building by adding materials, tasks, costs, experiments, or snapshots as needed.")

# Append the new method to MakerLedger
MakerLedger.suggest_next_action = suggest_next_action
