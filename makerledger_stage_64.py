# === Stage 64: Add validation for relationship references ===
# Project: MakerLedger
class ReferenceError(Exception):
    def __init__(self, model_name, ref_id):
        self.model_name = model_name
        self.ref_id = ref_id
        super().__init__(f"Invalid reference in {model_name}: #{ref_id}")


def validate_references(record):
    if isinstance(record, Material):
        return record.validate()

    if isinstance(record, Task):
        required = {"project": str, "status": (str, int)}
        for field, expected_type in required.items():
            val = getattr(record, field)
            if not isinstance(val, expected_type):
                raise ReferenceError("Task", record.id)

    if isinstance(record, Cost):
        return record.validate()

    if isinstance(record, Experiment):
        required = {"project": str, "status": (str, int)}
        for field, expected_type in required.items():
            val = getattr(record, field)
            if not isinstance(val, expected_type):
                raise ReferenceError("Experiment", record.id)

    if isinstance(record, Snapshot):
        return record.validate()

    raise ReferenceError("Unknown model", None)
