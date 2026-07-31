# === Stage 86: Add sample command transcripts for the main CLI workflows ===
# Project: MakerLedger
import subprocess, sys


def run_cli(args: list[str]) -> int:
    """Run a MakerLedger CLI command and return its exit code."""
    cmd = ["python", "-m", "makerledger"] + args
    print(">>> ", " ".join(cmd))
    result = subprocess.run(cmd)
    if result.stdout:
        print(result.stdout.decode())
    if result.stderr:
        sys.stderr.write(result.stderr.decode())
    return result.returncode


# ---- sample transcripts -------------------------------------------------

print("=" * 60)
print("Sample CLI workflows for MakerLedger")
print("=" * 60)

for label, args in [
    ("add material",    ["material", "wood", "--qty=3", "--cost=12.5"]),
    ("add task",        ["task", "frame", "--desc=Build frame"]),
    ("add cost",        ["cost", "nails", "--item=nails", "--qty=100", "--price=0.05"]),
    ("snapshot project","snapshot"),
]:
    print(f"\n--- {label} ---")
    rc = run_cli(args)
    if rc:
        print("ERROR (exit code {})".format(rc))
