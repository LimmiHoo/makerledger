# === Stage 53: Add command help text and usage examples ===
# Project: MakerLedger
def usage(self):
    """Return formatted help text and examples for MakerLedger."""
    lines = [
        "MakerLedger — Workshop Build Ledger",
        "",
        "Usage:",
        "    python makerledger.py <command> [options]",
        "",
        "Commands:",
        "  list           List all entries (materials, tasks, costs, experiments)",
        "  add            Add a new entry (specify type: material|task|cost|experiment)",
        "  delete         Remove an entry by index",
        "  snapshot       Save current ledger state to a JSON file",
        "",
        "Examples:",
        '    python makerledger.py list',
        '    python makerledger.py add --type material --name "LED Strip" --qty 5',
        '    python makerledger.py add --type cost --amount 29.99 --label "Wiring"',
        '    python makerledger.py snapshot --output ledger.json',
        '    python makerledger.py delete --index 0',
    ]
    return "\n".join(lines)
