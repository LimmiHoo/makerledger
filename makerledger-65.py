# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: MakerLedger
def merge_imports(existing: List[str], new: str) -> Tuple[List[str], bool]:
    """Add a line only if it does not already appear (modulo whitespace)."""
    normalized = re.sub(r"\s+", " ", existing.strip()).lower()
    if f" {new} ".strip().lower() in normalized:
        return existing, False
    existing.append(new)
    return existing, True
