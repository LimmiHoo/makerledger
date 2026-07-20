# === Stage 41: Add plain text import for a simple line-based format ===
# Project: MakerLedger
def parse_csv_line(line: str):
    """Parse a simple comma-separated line into a list of strings, stripping whitespace."""
    return [field.strip() for field in line.split(",")]


def write_csv_row(data: list[str], file_obj) -> None:
    """Write one row to the CSV-style text stream, adding a trailing newline."""
    file_obj.write(",".join(data) + "\n")


if __name__ == "__main__":
    sample = "item,count,value"
    parts = parse_csv_line(sample)
    print(parts)  # ['item', 'count', 'value']

    with open("ledger_sample.csv", "w") as f:
        write_csv_row(["screw", "12", "0.5"], f)
        write_csv_row(["bolt", "8", "1.2"], f)

    with open("ledger_sample.csv") as f:
        for line in f:
            print(parse_csv_line(line))
