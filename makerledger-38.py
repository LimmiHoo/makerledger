# === Stage 38: Add data integrity checks for broken references ===
# Project: MakerLedger
def check_integrity(records, expected_refs):
    """Validate that all referenced materials and tasks exist."""
    material_ids = set(r['id'] for r in records if 'material_id' in r)
    task_ids = set(r['id'] for r in records if 'task_id' in r)

    broken_materials = []
    for rec in records:
        if 'material_id' in rec and rec['material_id'] not in material_ids:
            broken_materials.append(rec['id'])

    broken_tasks = []
    for rec in records:
        if 'task_id' in rec and rec['task_id'] not in task_ids:
            broken_tasks.append(rec['id'])

    return {'broken_material_refs': broken_materials, 'broken_task_refs': broken_tasks}
