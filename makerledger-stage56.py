# === Stage 56: Add compact error classes for domain failures ===
# Project: MakerLedger
class MakerError(Exception):
    """Base domain error for MakerLedger."""
    pass


class MaterialNotFoundError(MakerError):
    def __init__(self, material_id: str) -> None:
        self.material_id = material_id
        super().__init__(f"Material '{material_id}' not found")


class TaskAlreadyExistsError(MakerError):
    def __init__(self, task_name: str) -> None:
        self.task_name = task_name
        super().__init__(f"Task '{task_name}' already exists")


class CostMismatchError(MakerError):
    def __init__(self, expected: float, actual: float) -> None:
        self.expected = expected
        self.actual = actual
        super().__init__(f"Cost mismatch: expected {expected}, got {actual}")


class SnapshotStateError(MakerError):
    def __init__(self, current_state: str, desired_state: str) -> None:
        self.current_state = current_state
        self.desired_state = desired_state
        super().__init__(f"Cannot transition from '{current_state}' to '{desired_state}'")


class ExperimentInvalidError(MakerError):
    def __init__(self, reason: str) -> None:
        self.reason = reason
        super().__init__(reason)


class LedgerCorruptionError(MakerError):
    def __init__(self, message: str = "Ledger data is corrupted") -> None:
        super().__init__(message)
