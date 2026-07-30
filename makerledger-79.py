# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: MakerLedger
import os, sys, json, datetime

def self_check():
    print("=== MakerLedger Self-Check ===")
    here = os.path.dirname(os.path.abspath(__file__))
    
    # Load ledger from disk (or empty dict if missing)
    path = os.path.join(here, "ledger.json")
    try:
        with open(path) as f:
            led = json.load(f)
        print("  [OK] ledger.json loaded:", len(led.get("materials", [])), "materials,", 
              len(led.get("tasks", [])), "tasks,", len(led.get("costs", [])), "costs")
    except Exception as e:
        led = {"materials": [], "tasks": [], "costs": [], "experiments": [], "snapshots": []}
        print("  [WARN] ledger.json not found, starting fresh:", e)
    
    # Validate structure
    for section in ["materials", "tasks", "costs", "experiments", "snapshots"]:
        assert isinstance(led.get(section), list), f"Invalid {section} type."
    print("  [OK] All sections present and typed as lists.")

    # Demo: add a test material, task, cost
    led.setdefault("materials", []).append({"id": f"{datetime.datetime.now():%Y%m%d%H%M%S}", "name": "Demo-Test-Material", "qty": 1})
    led.setdefault("tasks", []).append({"id": f"{datetime.datetime.now():%Y%m%d%H%M%S}", "title": "Run Self-Check Test Task", "done": False, "notes": "Auto-injected"})
    led.setdefault("costs", []).append({"item": "Demo-Test-Material", "amount": 0.01, "unit": "$", "date": datetime.datetime.now().strftime("%Y-%m-%d")})

    # Persist and reload to verify round-trip
    with open(path, "w") as f:
        json.dump(led, f, indent=2)
    
    with open(path) as f:
        led2 = json.load(f)
    assert len(led2["materials"]) >= 1 and len(led2["tasks"]) >= 1 and led2["costs"][-1]["item"] == "Demo-Test-Material", "Round-trip failed!"

    print("  [OK] Round-trip write/read verified.")
    print("\n=== MakerLedger Self-Check PASSED ===")

self_check()
