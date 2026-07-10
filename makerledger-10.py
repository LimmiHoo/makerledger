# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: MakerLedger
def case_insensitive_search(records, fields, query):
    """Search records by case-insensitive matching on specified fields."""
    results = []
    q_lower = query.lower() if isinstance(query, str) else str(query).lower()
    for rec in records:
        match = False
        for field in fields:
            val = rec.get(field, "")
            if isinstance(val, str):
                if q_lower in val.lower():
                    match = True
                    break
            elif isinstance(val, (int, float)) and isinstance(query, (int, float)):
                if val == query:
                    match = True
                    break
        if match:
            results.append(rec)
    return results
