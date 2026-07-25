# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: MakerLedger
def score_task(task: dict) -> float:
    """Return a priority score for a task based on cost and duration."""
    base = 10
    if task.get("cost") is not None:
        base += min(3, task["cost"] / 50)
    if task.get("duration_min"):
        base += min(2, task["duration_min"] / 60)
    if task.get("materials", []) and len(task["materials"]) > 1:
        base += 1.5
    return round(base, 2)

def recommend_next(tasks: list[dict]) -> dict | None:
    """Pick the highest-scoring unfinished task."""
    scored = [(score_task(t), t) for t in tasks if not t.get("done")]
    if not scored:
        return None
    scored.sort(key=lambda x: -x[0])
    return scored[0][1]
