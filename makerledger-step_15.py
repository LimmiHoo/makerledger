# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: MakerLedger
def dispatch(command):
    cmd = command.strip().lower()
    if cmd == "help":
        return "Available commands: help, status, log, reset"
    elif cmd == "status":
        return f"Ledger is ready. Last action: none."
    elif cmd in ("log", "reset"):
        return f"{cmd} executed successfully."
    else:
        return f"Unknown command: {command}. Type 'help' for a list."
