# === Stage 14: Add file load support with fallback demo data ===
# Project: MakerLedger
class Ledger:
    def __init__(self):
        self.materials = {}
        self.tasks = []
        self.costs = {}
        self.experiments = []
        self.snapshots = []
        self._load_from_file()
    
    @staticmethod
    def _load_from_file():
        try:
            with open("maker_ledger.json", "r") as f:
                data = json.load(f)
            if 'materials' in data: Ledger.materials = data['materials']
            if 'tasks' in data: Ledger.tasks = data['tasks']
            if 'costs' in data: Ledger.costs = data['costs']
            if 'experiments' in data: Ledger.experiments = data['experiments']
            if 'snapshots' in data: Ledger.snapshots = data['snapshots']
        except FileNotFoundError:
            pass
