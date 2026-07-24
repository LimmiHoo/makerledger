# === Stage 57: Add structured result objects for command handlers ===
# Project: MakerLedger
class Result:
    def __init__(self, status="ok", message="", data=None):
        self.status = status
        self.message = message
        self.data = data
        if data is None:
            self.data = []

    def to_dict(self):
        return {
            "status": self.status,
            "message": self.message,
            "data": self.data,
        }


def success(data=None, msg=""):
    r = Result(status="ok", message=msg)
    if data is not None:
        r.data.append(data)
    return r


def error(msg):
    return Result(status="error", message=msg)
