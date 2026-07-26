# === Stage 67: Add a function that returns key project metrics ===
# Project: MakerLedger
from collections import defaultdict

def project_metrics(ledger):
    """Return a summary dict of key metrics for the current ledger."""
    total_cost = sum(entry['cost'] for entry in ledger if 'cost' in entry)
    material_count = len([e for e in ledger if 'material' in e])
    task_count = len([e for e in ledger if 'task' in e])
    experiment_count = len([e for e in ledger if 'experiment' in e])
    snapshot_count = len([s for s in ledger if isinstance(s, dict) and s.get('type') == 'snapshot'])
    return {
        'total_cost': total_cost,
        'materials': material_count,
        'tasks': task_count,
        'experiments': experiment_count,
        'snapshots': snapshot_count,
    }
