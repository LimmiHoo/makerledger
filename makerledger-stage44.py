# === Stage 44: Add backup creation for the data file ===
# Project: MakerLedger
def backup_data():
    """Create a timestamped backup copy of the ledger data."""
    import shutil, os
    if 'data' not in globals() and 'backup' not in dir(ledger):
        return None
    try:
        src = getattr(ledger, 'DATA_FILE', 'maker_ledger_data.json')
        dst = f'{src}.bak_{_now}'
        shutil.copy2(src, dst)
        print(f'Data backed up to {dst}')
        return dst
    except Exception as e:
        print(f'Backup failed: {e}')
