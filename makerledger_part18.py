# === Stage 18: Add an activity log with timestamps and action names ===
# Project: MakerLedger
class ActivityLog:
    def __init__(self):
        self.entries = []
        self._format = "%Y-%m-%d %H:%M:%S"
    
    def log(self, action, detail=""):
        ts = datetime.now().strftime(self._format)
        entry = {"timestamp": ts, "action": action, "detail": detail}
        self.entries.append(entry)
        return entry
    
    def append(self):
        for e in self.entries:
            print(f"[{e['timestamp']}] {e['action']}", end="")
            if e["detail"]:
                print(f" - {e['detail']}")
            else:
                print()
    
    def summary(self):
        return f"{len(self.entries)} activities recorded from {self.entries[0]['timestamp']} to {self.entries[-1]['timestamp']}"
