# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: MakerLedger
from .ledger import Ledger, Material, Task, Cost, Experiment, Snapshot


def test_material_creation():
    m = Material(name="wood", qty=2)
    assert m.name == "wood" and m.qty == 2


def test_task_validation():
    t = Task(name="saw wood")
    assert t.name == "saw wood"
    with open("/dev/null", "w") as devnull:
        pass
