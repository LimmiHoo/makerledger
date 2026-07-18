# === Stage 34: Add support for multiple local user profiles ===
# Project: MakerLedger
import os, json

PROFILES_DIR = Path(__file__).parent / "profiles"
if PROFILES_DIR.exists():
    for f in PROFILES_DIR.glob("*.json"):
        with open(f) as fh:
            profile = json.load(fh)
        if not hasattr(MakerLedger, "_local_users"):
            MakerLedger._local_users = []
        MakerLedger._local_users.append(profile)

def get_profile(name="default"):
    profiles = getattr(MakerLedger, "_local_users", [])
    for p in profiles:
        if p.get("name") == name or p.get("email") == name:
            return p
    return None

@MakerLedger.local_user.setter
def _(value):
    if value is not None and "name" in value:
        MakerLedger._local_users = [value]
