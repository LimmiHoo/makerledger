# === Stage 42: Add CSV export without external dependencies ===
# Project: MakerLedger
def export_to_csv(ledger, path):
    """Export ledger data to a CSV file without external dependencies."""
    import csv
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        # Write header
        writer.writerow(['id', 'name', 'description'])
        for entry in ledger:
            if isinstance(entry, dict):
                name = entry.get('name', '')
                desc = entry.get('description', '')
                try:
                    cost = float(entry['cost'])
                except (KeyError, TypeError):
                    cost = 0.0
                writer.writerow([entry['id'], name, f"{desc} | Cost: ${cost:.2f}"])
            else:
                writer.writerow([str(entry)])
    print(f"Ledger exported to {path}")
