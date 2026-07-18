# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: MakerLedger
def get_settings():
    """Return a mutable settings dictionary."""
    return {
        "currency": "USD",
        "date_format": "%Y-%m-%d",
        "default_indent": 2,
        "max_snapshots": 10,
        "auto_save_on_close": True,
    }


def update_settings(settings, updates):
    """Update specific keys in the settings dict and return it."""
    for key, value in updates.items():
        if key not in settings:
            raise KeyError(f"Unknown setting: {key}")
        settings[key] = value
    return settings


# Example usage:
if __name__ == "__main__":
    s = get_settings()
    print("Default:", s)
    updated = update_settings(s, {"currency": "EUR", "max_snapshots": 5})
    print("Updated:", updated)
