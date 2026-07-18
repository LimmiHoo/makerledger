# === Stage 35: Add active user switching and user-specific records ===
# Project: MakerLedger
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.active = True

    def toggle_active(self):
        self.active = not self.active

    def __repr__(self):
        status = "active" if self.active else "inactive"
        return f"<User {self.name} ({status})>"


class UserLedger:
    def __init__(self, users=None):
        self.users = users or []

    def add_user(self, user):
        self.users.append(user)
        return user

    def get_active_users(self):
        return [u for u in self.users if u.active]

    def switch_active(self, name):
        for u in self.users:
            if u.name == name:
                u.toggle_active()
                active = self.get_active_users()
                if len(active) == 1 and active[0] != u:
                    active[0].toggle_active()
                return True
        return False

    def __repr__(self):
        active = self.get_active_users()
        return f"<UserLedger {len(self.users)} users, {len(active)} active>"
