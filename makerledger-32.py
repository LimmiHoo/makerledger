# === Stage 32: Add pagination helpers for long console output ===
# Project: MakerLedger
def paginate_output(lines, chunk=15):
    total = len(lines)
    for i in range(0, total, chunk):
        print(f"--- Page {i // chunk + 1} of {total // chunk + (1 if total % chunk else 0)} ---")
        for line in lines[i:i+chunk]:
            print(line.strip())

# Example usage:
output = [
    "Total materials used: 48",
    "Task count: 12",
    "Cost summary: $3,650.75",
    "Experiments run: 7",
    "Projects completed: 3",
]
paginate_output(output)
