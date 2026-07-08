# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: MakerLedger
from dataclasses import dataclass, field
from datetime import date


@dataclass
class Material:
    name: str
    quantity: float
    unit: str
    cost_per_unit: float = 0.0
    supplier: str = ""
    notes: str = ""

    @property
    def total_cost(self) -> float:
        return self.quantity * self.cost_per_unit


@dataclass
class Task:
    title: str
    description: str
    start_date: date
    end_date: date | None = None
    status: str = "planned"  # planned, in_progress, completed

    @property
    def duration_days(self) -> int:
        if self.end_date is None:
            return (date.today() - self.start_date).days
        return (self.end_date - self.start_date).days


@dataclass
class Experiment:
    name: str
    hypothesis: str
    method: str
    results_summary: str = ""
    observations: list[str] = field(default_factory=list)

    @property
    def is_validated(self) -> bool:
        return len(self.observations) > 0 and "success" in self.results_summary.lower()


@dataclass
class ProjectSnapshot:
    project_name: str
    snapshot_date: date
    materials_used: list[Material] = field(default_factory=list)
    tasks_completed: list[Task] = field(default_factory=list)
    total_cost: float = 0.0

    @property
    def summary(self) -> dict:
        return {
            "project": self.project_name,
            "date": str(self.snapshot_date),
            "materials_count": len(self.materials_used),
            "tasks_done": len(self.tasks_completed),
            "total_cost": round(self.total_cost, 2),
        }
