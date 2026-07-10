# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: MakerLedger
def format_material(m):
    return f"[{m.name}] qty={m.quantity} units, cost=${m.unit_cost:.2f}"

def format_task(t):
    status = "DONE" if t.is_complete else "OPEN"
    return f"[TASK] {t.title} | {status} | hours={t.hours:.1f}h | $${t.total_cost:.2f}"

def format_experiment(e):
    result = e.success and "SUCCESS" or "FAIL"
    return f"[EXP] {e.name} | {result} | notes=\"{e.notes}\""

def format_snapshot(s):
    total_materials = sum(m.unit_cost * m.quantity for m in s.material_log)
    total_tasks = sum(t.total_cost for t in s.task_log)
    return (f"[SNAPSHOT] project={s.project_name} | "
            f"dollar_total=${total_materials + total_tasks:.2f} | "
            f"tasks_done={sum(1 for t in s.task_log if t.is_complete)}")

def print_ledger_header():
    print("=" * 60)
    print("  MAKER LEDGER — Console View")
    print("=" * 60)

def print_materials(materials):
    print("\n--- Materials ---")
    for m in materials:
        print(format_material(m))

def print_tasks(tasks):
    print("\n--- Tasks ---")
    for t in tasks:
        print(format_task(t))

def print_experiments(experiments):
    print("\n--- Experiments ---")
    for e in experiments:
        print(format_experiment(e))

def print_snapshot(s):
    print("\n--- Project Snapshot ---")
    print(format_snapshot(s))
