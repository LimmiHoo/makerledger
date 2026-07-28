# === Stage 73: Add a lightweight HTML report export ===
# Project: MakerLedger
import json, os
from pathlib import Path


class ReportExporter:
    """Lightweight HTML report export for MakerLedger."""

    def __init__(self, ledger_path):
        self.ledger_path = Path(ledger_path)

    def load_ledger(self):
        with open(self.ledger_path) as f:
            return json.load(f)

    def generate_html(self, data):
        html_parts = [
            "<!DOCTYPE html>",
            "<html><head><meta charset='utf-8'>",
            "<title>MakerLedger Report</title>",
            "<style>body{font-family:sans-serif;max-width:900px;margin:2em auto;padding:1em;}table{border-collapse:collapse;width:100%;margin-bottom:1.5em;}th,td{border:1px solid #ccc;padding:.4em 1em;text-align:left;}th{background:#f5f5f5;}</style></head><body>",
        ]
        html_parts.append(f"<h1>MakerLedger Report</h1>")

        if "materials" in data:
            html_parts.append("<h2>Materials</h2><table><tr><th>ID</th><th>Name</th><th>Quantity</th><th>Unit Cost</th></tr>")
            for m in data["materials"]:
                html_parts.append(f"<tr><td>{m.get('id', '')}</td><td>{m.get('name', '')}</td><td>{m.get('quantity', 0)}</td><td>${m.get('unit_cost', 0):.2f}</td></tr>")
            html_parts.append("</table>")

        if "tasks" in data:
            html_parts.append("<h2>Tasks</h2><table><tr><th>ID</th><th>Title</th><th>Status</th><th>Cost</th></tr>")
            for t in data["tasks"]:
                html_parts.append(f"<tr><td>{t.get('id', '')}</td><td>{t.get('title', '')}</td><td>{t.get('status', '')}</td><td>${t.get('cost', 0):.2f}</td></tr>")
            html_parts.append("</table>")

        if "experiments" in data:
            html_parts.append("<h2>Experiments</h2><ul>")
            for e in data["experiments"]:
                html_parts.append(f"<li>{e.get('title', '')} — {e.get('observation', '')}</li>")
            html_parts.append("</ul>")

        if "snapshots" in data:
            html_parts.append("<h2>Project Snapshots</h2><table><tr><th>Date</th><th>Description</th></tr>")
            for s in data["snapshots"]:
                html_parts.append(f"<tr><td>{s.get('date', '')}</td><td>{s.get('description', '')}</td></tr>")
            html_parts.append("</table>")

        if "cost_summary" in data:
            total = sum(t.get("cost", 0) for t in data.get("tasks", [])) + sum(m.get("unit_cost", 0) * m.get("quantity", 1) for m in data.get("materials", []))
            html_parts.append(f"<h2>Cost Summary</h2><p>Total Cost: ${total:.2f}</p>")

        html_parts.append("</body></html>")
        return "\n".join(html_parts)

    def export(self, output_path="maker_ledger_report.html"):
        data = self.load_ledger()
        html = self.generate_html(data)
        with open(output_path, "w") as f:
            f.write(html)
        print(f"Report exported to {output_path}")


if __name__ == "__main__":
    exporter = ReportExporter("./ledger.json")
    exporter.export()
