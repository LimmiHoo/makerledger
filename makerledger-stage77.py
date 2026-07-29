# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: MakerLedger
def load_entry(filepath: str) -> dict:
    with open(filepath, encoding="utf-8") as f:
        return json.load(f)


def save_entry(entry: dict, filepath: str) -> None:
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(entry, f, indent=2, sort_keys=True)


def load_project(project_id: str) -> Optional[dict]:
    return _load_from_db("projects", project_id)


def save_project(project: dict) -> None:
    _save_to_db("projects", project)


def load_materials() -> list[dict]:
    return _load_all("materials")


def save_material(material: dict) -> None:
    _save_to_db("materials", material)


def load_tasks() -> list[dict]:
    return _load_all("tasks")


def save_task(task: dict) -> None:
    _save_to_db("tasks", task)


def load_costs() -> list[dict]:
    return _load_all("costs")


def save_cost(cost: dict) -> None:
    _save_to_db("costs", cost)


def load_experiments() -> list[dict]:
    return _load_all("experiments")


def save_experiment(experiment: dict) -> None:
    _save_to_db("experiments", experiment)


def load_snapshots() -> list[dict]:
    return _load_all("snapshots")


def save_snapshot(snapshot: dict) -> None:
    _save_to_db("snapshots", snapshot)


def print_summary() -> None:
    for item in load_project("current"):
        print(f"{item['type']}: {item.get('name', 'unnamed')} — cost: ${item.get('total_cost', 0):.2f}")
