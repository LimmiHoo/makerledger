# === Stage 80: Polish user-facing messages, names, and examples for consistency ===
# Project: MakerLedger
def print_project_report(project: Project) -> None:
    """Print a polished, user-facing summary of any project."""
    print(f"{'='*60}")
    print(f"  PROJECT REPORT — {project.name}")
    print(f"{'='*60}")
    if project.description:
        print(f"\n  Description : {project.description}")

    material_rows = sorted(
        [(m.amount, m.unit, m.note) for m in project.materials],
        key=lambda r: r[0] or 0,
    )
    print("\n  Materials (sorted by amount)")
    if material_rows:
        print(f"  {'Amount':>12}   Unit      Note")
        for amt, unit, note in material_rows:
            print(f"  {amt:>12}     {unit:<8} {note}")

    cost_rows = sorted(
        [(c.amount, c.unit, c.note) for c in project.costs],
        key=lambda r: r[0] or 0,
    )
    print("\n  Costs (sorted by amount)")
    if cost_rows:
        print(f"  {'Amount':>12}   Unit      Note")
        for amt, unit, note in cost_rows:
            print(f"  {amt:>12}     {unit:<8} {note}")

    task_rows = sorted(
        [(t.name, t.done) for t in project.tasks],
        key=lambda r: not r[1],
    )
    print("\n  Tasks")
    if task_rows:
        print(f"  {'Name':<25} Done")
        for name, done in task_rows:
            mark = "✓" if done else "○"
            print(f"  {name:<25} {mark}")

    exp_rows = sorted(
        [(e.name, e.success) for e in project.experiments],
        key=lambda r: not r[1],
    )
    print("\n  Experiments")
    if exp_rows:
        print(f"  {'Name':<25} Success")
        for name, success in exp_rows:
            mark = "✓" if success else "✗"
            print(f"  {name:<25} {mark}")

    snapshot = project.snapshot
    if snapshot is not None and len(snapshot):
        snap = snapshot[0]
        print("\n  Latest Snapshot")
        print(f"  Date      : {snap.date}")
        print(f"  Status    : {snap.status}")
        if snap.notes:
            print(f"  Notes     : {snap.notes}")

    print()
