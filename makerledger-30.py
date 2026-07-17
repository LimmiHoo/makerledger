# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: MakerLedger
import re


def parse_date(date_string):
    """Parse date strings in ISO (YYYY-MM-DD), US (MM/DD/YYYY), and DD.MM.YYYY format."""
    if not date_string or not isinstance(date_string, str):
        raise ValueError("Input must be a non-empty string.")

    patterns = [
        (r'^\d{4}-\d{2}-\d{2}$', '%Y-%m-%d'),
        (r'^\d{1,2}/\d{1,2}/\d{4}$', '%m/%d/%Y'),
        (r'^\d{1,2}\.\d{1,2}\.\d{4}$', '%d.%m.%Y'),
    ]

    for pattern, fmt in patterns:
        if re.match(pattern, date_string):
            return datetime.strptime(date_string.strip(), fmt).date()

    raise ValueError(
        f"Unrecognized date format. Expected ISO (YYYY-MM-DD), US (MM/DD/YYYY), "
        f"or European (DD.MM.YYYY). Got: {date_string!r}"
    )
