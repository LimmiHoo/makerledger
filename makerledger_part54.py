# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: MakerLedger
def colorize(text, code):
    """Print text wrapped in ANSI color codes."""
    print(f"\033[{code}m{text}\033[0m")
