# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: MakerLedger
import os, json, shutil
from pathlib import Path

def test_update_edge_cases():
    from makerledger.models import Entry, Task, Cost, Material
    from makerledger.storage import InMemoryStore

    store = InMemoryStore()
    task = Task("test_task", "desc", 10)
    cost = Cost("c1", 5.0, "tool")
    material = Material("m1", "steel", 2.0, 3.0)

    entry = Entry(task=task, costs=[cost], materials=[material])
    store.create_entry(entry)
    updated = store.update_entry(
        store.get_key(entry),
        entry._replace(costs=[Cost("c1", 6.0, "tool")]),
    )
    assert updated.costs[0].value == 6.0

def test_delete_edge_cases():
    from makerledger.models import Entry, Task, Cost
    from makerledger.storage import InMemoryStore

    store = InMemoryStore()
    task = Task("d1", "delete me", 1)
    cost = Cost("dc1", 0.5, "screw")
    entry = Entry(task=task, costs=[cost])
    store.create_entry(entry)
    key = store.get_key(entry)
    assert store.exists(key), "entry should exist"
    store.delete_entry(store.get_key(entry))
    assert not store.exists(key), "entry should be gone after delete"

if __name__ == "__main__":
    test_update_edge_cases()
    test_delete_edge_cases()
