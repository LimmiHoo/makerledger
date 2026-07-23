# === Stage 50: Add unit tests for import and export behavior ===
# Project: MakerLedger
import os, json, pytest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "makerledger"


def _read(src_path: str) -> dict:
    path = SRC / src_path
    assert path.exists(), f"Missing source file {path}"
    return json.loads(path.read_text())


class TestImportExport:
    def test_materials_roundtrip(self):
        data = _read("materials.json")
        assert isinstance(data, dict) and "materials" in data

    def test_tasks_roundtrip(self):
        data = _read("tasks.json")
        assert isinstance(data, dict) and "tasks" in data

    def test_costs_roundtrip(self):
        data = _read("costs.json")
        assert isinstance(data, dict) and "entries" in data

    def test_experiments_roundtrip(self):
        data = _read("experiments.json")
        assert isinstance(data, dict) and "experiments" in data

    def test_snapshots_roundtrip(self):
        data = _read("snapshots.json")
        assert isinstance(data, dict) and "snapshots" in data
