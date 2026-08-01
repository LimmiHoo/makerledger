# === Stage 88: Add safer defaults for empty input and missing optional fields ===
# Project: MakerLedger
def _coerce_int(value, default=0):
    """Convert string or numeric input to int safely."""
    if value is None:
        return default
    try:
        return int(float(value))
    except (ValueError, TypeError):
        pass
    return default

def _coerce_float(value, default=0.0):
    """Convert string or numeric input to float safely."""
    if value is None:
        return default
    try:
        return float(value)
    except (ValueError, TypeError):
        pass
    return default

def _coerce_bool(value, default=False):
    """Convert various truthy inputs to bool safely."""
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        lower = value.strip().lower()
        return lower in ("true", "1", "yes")
    try:
        return bool(int(value))
    except (ValueError, TypeError):
        pass
    return default

def _coerce_str(value, default=""):
    """Convert input to string safely."""
    if value is None:
        return default
    return str(value)

class LedgerEntry:
    def __init__(self, **kwargs):
        self.project_id = kwargs.get("project_id", 0)
        self.entry_type = kwargs.get("entry_type", "")
        self.description = kwargs.get("description", "")
        self.quantity = _coerce_int(kwargs.get("quantity"))
        self.unit_price = _coerce_float(kwargs.get("unit_price"))
        self.total_cost = _coerce_float(kwargs.get("total_cost"))
        self.date = kwargs.get("date", None)
        self.status = _coerce_str(kwargs.get("status"), "")
