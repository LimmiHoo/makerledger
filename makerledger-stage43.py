# === Stage 43: Add CSV import for the primary record type ===
# Project: MakerLedger
import csv, io


def import_ledger_from_csv(csv_text: str) -> list[dict]:
    """Read a CSV ledger with columns: id, name, type, date, cost."""
    reader = csv.DictReader(io.StringIO(csv_text))
    records = []
    for row in reader:
        try:
            rec = {
                "id": int(row["id"]) if row.get("id") else None,
                "name": row["name"],
                "type": row["type"],
                "date": row["date"],
                "cost": float(row["cost"]) if row.get("cost") and row["cost"] != "" else 0.0,
            }
        except (KeyError, ValueError):
            continue
        records.append(rec)
    return records


if __name__ == "__main__":
    sample = "id,name,type,date,cost\n1,MudBrick,material,2024-03-01,5.75\n2,LoomBuild,experiment,2024-03-02,0.0"
    for r in import_ledger_from_csv(sample):
        print(r)
