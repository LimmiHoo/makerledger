# === Stage 72: Add Markdown report export ===
# Project: MakerLedger
class ReportExporter:
    def __init__(self, project):
        self.project = project

    def export(self):
        lines = [f"# MakerLedger Report - {self.project.name}\n"]
        for key in ["materials", "tasks", "costs", "experiments"]:
            if hasattr(self.project, key) and getattr(self.project, key):
                items = getattr(self.project, key)
                if isinstance(items, list):
                    lines.append(f"\n## {key.title().replace('_', ' ')}\n")
                    for item in items:
                        lines.append(f"- **{item.get('name', 'N/A')}**: {item.get('summary', '')}")
        return "\n".join(lines) + "\n"
