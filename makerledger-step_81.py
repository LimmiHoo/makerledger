# === Stage 81: Add final README text as a module string with usage examples ===
# Project: MakerLedger
USAGE_EXAMPLE = """\
# MakerLedger – Quick Start Guide
# ===============================

## 1. Initialize a project
    from maker_ledger import Ledger, Material, Task, Cost, Experiment, Snapshot
    ledger = Ledger("Workshop Build")
    snapshot = Snapshot(ledger)  # records current state

## 2. Add materials and costs
    steel = Material("Steel Sheet", qty=5, unit="kg", cost_per_unit=12.50, supplier="MetalCorp")
    solder = Material("Solder Wire", qty=100, unit="m", cost_per_unit=0.75, supplier="ElectroSupply")

    steel_cost = Cost(steel, quantity_used=3, waste_factor=0.02)   # 2% waste allowed
    solder_cost = Cost(solder, quantity_used=40, waste_factor=0.01)

## 3. Log tasks and experiments
    task_assembly = Task("Frame Assembly", duration_min=90, status="completed")
    task_wiring   = Task("Wiring Harness", duration_min=45, status="in_progress")

    exp_heat_test = Experiment("Heat Resistance Test", notes="Ran at 120°C for 30 min", result="passed", timestamp=None)

## 4. Record costs and update snapshot
    ledger.add_cost(steel_cost)
    ledger.add_cost(solder_cost)
    ledger.log_task(task_assembly)
    ledger.log_experiment(exp_heat_test)
    snapshot.update()  # persists all changes to current state

## 5. Generate a report from the ledger
    print(f"Total cost: {ledger.get_total_cost():.2f}")
    print(f"In-progress tasks: {sum(1 for t in ledger.tasks if t.status == 'in_progress')}")
    snapshot.export("project_report.csv")
"""
