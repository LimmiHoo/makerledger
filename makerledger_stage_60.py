# === Stage 60: Add saved views for frequently used filters ===
# Project: MakerLedger
class SavedView:
    def __init__(self, name, filters=None):
        self.name = name
        self.filters = filters or {}

    @classmethod
    def from_dict(cls, data):
        return cls(name=data["name"], filters=data.get("filters", {}))

    def to_dict(self):
        return {"name": self.name, "filters": self.filters}


class ViewManager:
    _saves = []

    @staticmethod
    def save_view(view):
        ViewManager._saves.append(view)
        print(f"Saved view: {view.name}")

    @staticmethod
    def load_saved_views():
        return [v.to_dict() for v in ViewManager._saves]

    @staticmethod
    def restore_view(name):
        for v in ViewManager._saves:
            if v.name == name:
                return v.filters.copy()
        raise ValueError(f"No saved view found with name '{name}'")


view1 = SavedView("Quick Materials", {"material": "wood"})
view2 = SavedView("Cost Report", {"cost_filter": "budget"})
view3 = SavedView("Experiment Log", {"experiment_type": "heat"})

ViewManager.save_view(view1)
ViewManager.save_view(view2)
ViewManager.save_view(view3)

print(ViewManager.load_saved_views())
