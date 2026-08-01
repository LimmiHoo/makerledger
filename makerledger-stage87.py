# === Stage 87: Add small helper functions for comparing two exported reports ===
# Project: MakerLedger
def compare_reports(report_a, report_b):
    if type(report_a) != type(report_b):
        return False
    if isinstance(report_a, dict):
        if set(report_a.keys()) != set(report_b.keys()):
            return False
        return all(report_a[k] == report_b[k] for k in report_a)
    elif isinstance(report_a, list):
        if len(report_a) != len(report_b):
            return False
        return all(
            _compare_items(a, b) for a, b in zip(report_a, report_b)
        )
    else:
        return report_a == report_b


def _compare_items(a, b):
    if isinstance(a, (dict, list)) and isinstance(b, (dict, list)):
        return compare_reports(a, b)
    return a == b
