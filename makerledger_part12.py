# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: MakerLedger
def load_json_safe(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except (json.JSONDecodeError, ValueError) as exc:
        print(f"Warning: {path} is malformed — skipping: {exc}")
        return None
