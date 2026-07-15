# === Stage 19: Add undo support for the last simple mutation ===
# Project: MakerLedger
import bisect, json, os

def undo_last(project_path):
    """Undo the most recent mutation by restoring from an earlier snapshot."""
    with open(os.path.join(project_path, 'snapshots.json'), 'r') as f:
        snapshots = json.load(f)
    if not snapshots:
        print("No snapshots to revert.")
        return
    # Sort timestamps and pick the one just before the last entry
    sorted_snap = sorted(snapshots, key=lambda s: s['timestamp'])
    latest = sorted_snap[-1]
    # Find the previous snapshot; if none exists, warn
    prev_idx = len(sorted_snap) - 2
    if prev_idx < 0:
        print("Only one snapshot exists; cannot undo.")
        return
    prev = sorted_snap[prev_idx]
    with open(os.path.join(project_path, 'ledger.json'), 'r') as f:
        ledger = json.load(f)
    # Replace current state with the previous snapshot's data
    for key in ('materials', 'tasks', 'costs', 'experiments'):
        if key in prev and key not in ledger or ledger.get(key, {}).get('entries') != prev.get(key, {}).get('entries'):
            ledger[key] = dict(prev[key])
    with open(os.path.join(project_path, 'ledger.json'), 'w') as f:
        json.dump(ledger, f, indent=2)
    print(f"Reverted to snapshot from {prev['timestamp']}.")

if __name__ == '__main__':
    undo_last('maker_ledger_project')
