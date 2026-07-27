# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: MakerLedger
import json, os, sys

CLEAR_FLAG_FILE = "clear_state_flag.txt"
LEDGER_DB_PATH = "ledger.json"


def clear_ledger_state():
    """Reset the ledger to a clean state and remove the database file."""
    if not os.path.exists(CLEAR_FLAG_FILE):
        print("Error: No active flag found. Run 'start' first.")
        sys.exit(1)

    try:
        with open(LEDGER_DB_PATH, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    for key in ["materials", "tasks", "costs", "experiments", "snapshots"]:
        if key in data:
            data[key].clear()

    with open(LEDGER_DB_PATH, "w") as f:
        json.dump(data, f, indent=2)

    os.remove(CLEAR_FLAG_FILE)
    print("Ledger state cleared successfully.")


def start():
    """Initialize the ledger and set the clear-state flag."""
    try:
        with open(LEDGER_DB_PATH, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    for key in ["materials", "tasks", "costs", "experiments", "snapshots"]:
        if key not in data:
            data[key] = []

    with open(LEDGER_DB_PATH, "w") as f:
        json.dump(data, f, indent=2)

    with open(CLEAR_FLAG_FILE, "w") as f:
        f.write("true")

    print("Ledger started. Use 'clear' to reset state.")


if __name__ == "__main__":
    cmd = input("Enter command (start/clear): ").strip().lower()
    if cmd == "start":
        start()
    elif cmd == "clear":
        clear_ledger_state()
