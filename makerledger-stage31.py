# === Stage 31: Add compact table rendering for long lists ===
# Project: MakerLedger
def compact_table(rows, headers=None):
    if not rows:
        return ""
    if headers is None:
        headers = list(rows[0])
    col_widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(val)))
    fmt = " | ".join(f"{{:<{w}}}" for w in col_widths) + " |"
    line = fmt.format(*headers).strip()
    sep = "-+-".join("-" * w for w in col_widths) + "-"
    lines = [line, sep]
    for row in rows:
        lines.append(fmt.format(*[str(v) for v in row]).strip())
    return "\n".join(lines)

def show_snapshots(data):
    if not data.get("projects"):
        print("No snapshots to display.")
        return
    headers = ["Project", "Status", "Date"]
    rows = []
    for p in data["projects"]:
        rows.append([p.get("name", ""), p.get("status", ""), p.get("date", "")])
    print(compact_table(rows, headers))

def show_materials(data):
    if not data.get("materials"):
        return
    headers = ["Name", "Qty", "Unit"]
    rows = [[m["name"], m["qty"], m["unit"]] for m in data["materials"]]
    print(compact_table(rows, headers))

def show_tasks(data):
    if not data.get("tasks"):
        return
    headers = ["Task", "Completed"]
    rows = [[t["title"], str(t["done"]).lower()] for t in data["tasks"]]
    print(compact_table(rows, headers))

def show_costs(data):
    total = sum(c["amount"] for c in data.get("costs", []))
    if not data.get("costs"):
        return
    rows = [[c["desc"], f"${c['amount']:.2f}"] for c in data["costs"]]
    print(compact_table(rows, ["Description", "Amount"]))
    print(f"Total: ${total:.2f}")

def show_experiments(data):
    if not data.get("experiments"):
        return
    headers = ["Title", "Result"]
    rows = [[e["title"], e.get("result", "")] for e in data["experiments"]]
    print(compact_table(rows, headers))
