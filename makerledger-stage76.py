# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: MakerLedger
import signal, sys

def handle_signal(signum, frame):
    print("\nInterrupted – flushing ledger and exiting…")
    try:
        from maker_ledger.cli import flush_ledger
        flush_ledger()
    except Exception as e:  # noqa: BLE001
        print(f"Flush error: {e}")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_signal)
