# === Stage 83: Add regression tests for the final demo workflow ===
# Project: MakerLedger
import pytest
from makerledger.models import Project, Material, Task, Cost, Experiment


def test_full_demo_workflow():
    project = Project(name="Workshop Demo", owner="alice")
    mat = Material(name="LED Strip", qty=2)
    task = Task(name="Assemble Frame", deps=["cut wood"])
    cost = Cost(item="Screw Pack", amount=5.99)
    exp = Experiment(name="Light Test", result="Success")

    project.add_material(mat)
    project.add_task(task)
    project.add_cost(cost)
    project.add_experiment(exp)

    assert len(project.materials) == 1
    assert len(project.tasks) == 1
    assert len(project.costs) == 1
    assert len(project.experiments) == 1
