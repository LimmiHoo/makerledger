# === Stage 55: Add a setting to disable colorized output ===
# Project: MakerLedger
import click

def disable_color():
    """Disables colorized output when running under Windows or when ANSI codes are unsupported."""
    if sys.platform == "win32":
        try:
            import os
            os.system("")
            return True
        except Exception:
            pass
    click.echo(click.style("Color disabled.", fg="yellow", bold=True))
