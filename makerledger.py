# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: MakerLedger
from dataclasses import dataclass, field
from datetime import date, timedelta
import random

@dataclass
class Material:
    name: str
    quantity: float
    unit_cost: float
    used_date: date = None

@dataclass
class Task:
    title: str
    description: str
    hours: int
    hourly_rate: float
    started_on: date
    completed_on: date

@dataclass
class Cost:
    category: str  # "materials" or "labor"
    items: list = field(default_factory=list)

@dataclass
class Experiment:
    name: str
    hypothesis: str
    outcome: str
    notes: str = ""

@dataclass
class ProjectSnapshot:
    date: date
    total_material_cost: float
    total_labor_cost: float
    tasks_completed: int

class MakerLedger:
    def __init__(self):
        self.materials = []
        self.tasks = []
        self.costs = {"materials": [], "labor": []}
        self.experiments = []
        self.snapshots = []

    def add_material(self, name, quantity, unit_cost, used_date=None):
        m = Material(name, quantity, unit_cost, used_date or date.today())
        self.materials.append(m)
        return m

    def complete_task(self, title, description, hours, hourly_rate, started_on, completed_on):
        t = Task(title, description, hours, hourly_rate, started_on, completed_on)
        self.tasks.append(t)
        if t.completed_on not in (s.date for s in self.snapshots):
            mat_cost = sum(m.quantity * m.unit_cost for m in self.materials if m.used_date <= t.completed_on)
            labor = sum(t2.hours * t2.hourly_rate for t2 in self.tasks if t2.completed_on == t.completed_on)
            snap = ProjectSnapshot(t.completed_on, mat_cost, labor, len(self.tasks))
            self.snapshots.append(snap)
        return t

    def record_experiment(self, name, hypothesis, outcome, notes=""):
        e = Experiment(name, hypothesis, outcome, notes)
        self.experiments.append(e)
