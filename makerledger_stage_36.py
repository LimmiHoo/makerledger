# === Stage 36: Add templates for quickly creating common records ===
# Project: MakerLedger
class RecordTemplate:
    """Factory for common ledger records."""

    @staticmethod
    def material(name, qty, unit, cost):
        return MaterialRecord(name=name, quantity=qty, unit=unit, cost_per_unit=cost)

    @staticmethod
    def task(title, description=""):
        return TaskRecord(title=title, description=description)

    @staticmethod
    def experiment(name, hypothesis="", result=""):
        return ExperimentRecord(name=name, hypothesis=hypothesis, result=result)

    @staticmethod
    def cost(label, amount):
        return CostRecord(label=label, amount=amount)
