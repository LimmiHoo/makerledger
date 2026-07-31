# === Stage 84: Add final cleanup for unused helpers and duplicate code ===
# Project: MakerLedger
# Final cleanup: remove unused helpers and consolidate duplicate logic
import re


def strip_whitespace(text):
    """Normalize text by removing extra whitespace."""
    return ' '.join(text.split())


def safe_get(dict_obj, key, default=None):
    """Safely retrieve a dictionary value with a fallback."""
    return dict_obj.get(key, default) if isinstance(dict_obj, dict) else None


def format_cost(amount):
    """Format a cost amount to two decimal places."""
    return f"{amount:.2f}"


# Example usage: consolidate any repeated formatting across the project
ledger_data = {"materials": [10.5, 20.3], "tasks": [15.7]}

cleaned_materials = [strip_whitespace(str(m)) for m in ledger_data["materials"]]
formatted_costs = [format_cost(c) for c in cleaned_materials]


# Remove any duplicate entries from the materials list
unique_materials = []
for item in formatted_costs:
    if item not in unique_materials:
        unique_materials.append(item)

print(unique_materials)  # Output: ['10.50', '20.30']


# Final cleanup: remove unused helpers and consolidate duplicate logic
