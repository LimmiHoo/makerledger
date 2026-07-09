# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: MakerLedger
def validate_field(value, field_name):
    if value is None:
        raise ValueError(f"Field '{field_name}' must not be empty")
    return True

def validate_identifier(identifier):
    if not identifier or len(identifier) < 3:
        raise ValueError("Identifier must have at least 3 characters")
    return True

def validate_short_text(text, max_length=50):
    if text is None or len(text.strip()) == 0:
        raise ValueError(f"Short text field cannot be empty (max {max_length} chars)")
    if len(text) > max_length:
        raise ValueError(f"Text exceeds maximum length of {max_length} characters")
    return True

def validate_cost(cost):
    try:
        cost = float(cost)
        if cost < 0:
            raise ValueError("Cost cannot be negative")
        return cost
    except (TypeError, ValueError):
        raise ValueError("Invalid cost format. Must be a number >= 0")
