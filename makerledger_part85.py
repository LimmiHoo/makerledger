# === Stage 85: Add final readiness report summarizing features and known limits ===
# Project: MakerLedger
def readiness_report():
    """Summarize MakerLedger features and known limits."""
    print("=== MakerLedger Readiness Report ===")
    print(f"Features:")
    print("  - Materials: store, list, and filter workshop components.")
    print("  - Tasks: define build steps with owners and due dates.")
    print("  - Costs: track per-task and overall project spending.")
    print("  - Experiments: record trials with outcomes for iteration.")
    print("  - Snapshots: save full project state at any point in time.")
    print(f"Known Limits:")
    print("  - No database; data lives in memory only (reset on restart).")
    print("  - Single-user, single-process usage assumed.")
    print("  - No authentication or access control built-in.")
    print("  - Input validation is basic; external injection not tested.")
    print("  - Not designed for concurrent writers to the same ledger.")

if __name__ == "__main__":
    readiness_report()
