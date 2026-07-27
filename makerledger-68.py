# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: MakerLedger
class Changelog:
    def __init__(self, log):
        self.log = log
    
    def compact(self):
        lines = []
        for date, events in sorted(self.log.items()):
            if not events:
                continue
            line = f"{date}:"
            distinct = set()
            for ev in events:
                distinct.add(ev)
            for e in sorted(distinct):
                line += " " + str(e)
            lines.append(line)
        return "\n".join(lines)
