# === Stage 63: Add relationships between records where useful ===
# Project: MakerLedger
def link_records(records):
    """Add cross-references between records where useful."""
    linked = {}
    for rec in records:
        ref_id = f"{rec['type']}:{rec['id']}" if 'id' in rec else None
        if ref_id and rec.get('related_to'):
            target = (rec['related_to']['type'], rec['related_to'].get('id'))
            linked.setdefault(ref_id, []).append(target)
    return {k: v for k, v in linked.items() if len(v) > 1}
