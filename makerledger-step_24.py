# === Stage 24: Add grouped summaries by category or status ===
# Project: MakerLedger
def grouped_summary(records, key_fn=None):
    if key_fn is None:
        key_fn = lambda r: getattr(r, 'category', r.get('status', 'unknown'))
    groups = {}
    for rec in records:
        k = str(key_fn(rec))
        groups.setdefault(k, []).append(rec)
    return [(k, sorted(v, key=lambda x: x['total_cost'] if isinstance(x, dict) else getattr(x, 'total_cost', 0))) for k, v in groups.items()]
